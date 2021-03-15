def  print_rhumbus(n):
    for i in range(n):
        indent = " " * (n - i - 1)
        stars = "* " * (i + 1)
        print(f"{indent}{stars}")

    for i in range(n - 2, -1, -1):
        indent = " " * (n - i - 1)
        stars = "* " * (i + 1)
        print(f"{indent}{stars}")

print_rhumbus(int(input("Брой редове: ")))