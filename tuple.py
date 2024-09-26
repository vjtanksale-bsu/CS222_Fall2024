def add(num0: int, num1: int) -> int:
    return num0 + num1
def QuotientRemainder(num0: int, num1: int) -> tuple[int, int]:
    return (num0 // num1, num0 % num1)
def GenerateSeries(start: float, stop: float, step: float) -> list[float]:
    return [value for value in range(int(start), int(stop), int(step))]
def main():
    print(GenerateSeries(10.0, 1000.0, 50.0))
main()