"""Создаёт сводную Markdown-таблицу из JUnit XML-отчётов pytest."""

import sys
import xml.etree.ElementTree as ET
from pathlib import Path


def read_suite(xml_path: Path) -> dict:
    root = ET.parse(str(xml_path)).getroot()
    suites = [root] if root.tag == "testsuite" else list(root.iter("testsuite"))
    tests = failures = errors = skipped = 0
    duration = 0.0
    problems = []
    for suite in suites:
        tests += int(suite.get("tests", 0))
        failures += int(suite.get("failures", 0))
        errors += int(suite.get("errors", 0))
        skipped += int(suite.get("skipped", 0))
        duration += float(suite.get("time", 0))
        for case in suite.iter("testcase"):
            for kind in ("failure", "error"):
                node = case.find(kind)
                if node is not None:
                    message = (node.get("message") or (node.text or kind)).strip().splitlines()
                    problems.append(("{}::{}".format(case.get("classname"), case.get("name")),
                                     message[0] if message else kind))
    return {
        "tests": tests,
        "failures": failures,
        "errors": errors,
        "skipped": skipped,
        "passed": tests - failures - errors - skipped,
        "time": duration,
        "problems": problems,
    }


def main(artifacts_dir: str) -> int:
    root = Path(artifacts_dir)
    rows = {}
    for xml_path in sorted(root.glob("junit-*/test-results.xml")):
        rows[xml_path.parent.name.removeprefix("junit-")] = read_suite(xml_path)

    if not rows:
        print("## Сравнение версий модуля\n\nJUnit-отчёты не найдены.")
        return 1

    print("## Сравнение версий TemperatureConverter\n")
    print("| Ветка | Результат | Всего | Passed | Failed | Errors | Skipped | Время тестов, с |")
    print("|---|---:|---:|---:|---:|---:|---:|---:|")
    for name, result in rows.items():
        ok = result["failures"] == 0 and result["errors"] == 0
        status = "Успешно" if ok else "Есть ошибки"
        print("| {} | {} | {} | {} | {} | {} | {} | {:.3f} |".format(
            name, status, result["tests"], result["passed"], result["failures"],
            result["errors"], result["skipped"], result["time"]))

    for name, result in rows.items():
        if result["problems"]:
            print("\n### Ошибки: {}\n".format(name))
            for test_name, message in result["problems"]:
                print("- `{}` — {}".format(test_name, message))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "artifacts"))
