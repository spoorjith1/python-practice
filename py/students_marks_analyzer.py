def analyze_marks(marks):
    total = sum(marks)
    average = total / len(marks)
    highest = max(marks)
    lowest = min(marks)

    return total, average, highest, lowest


def main():
    print("Student Marks Analyzer")
    print("x--------------------x")

    n = int(input("Enter number of students: "))
    marks = []

    for i in range(n):
        m = float(input(f"Enter marks of student[{i+1}]: "))
        marks.append(m)

    total, avg, high, low = analyze_marks(marks)

    print()
    print("x--- Results ---x")
    print(f"Total Marks : {total}")
    print(f"Average Marks : {avg:.2f}")
    print(f"Highest Marks : {high}")
    print(f"Lowest Marks : {low}")


if __name__ == "__main__":
    main()
