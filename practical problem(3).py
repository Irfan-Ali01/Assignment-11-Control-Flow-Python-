def type_triangle(s1, s2, s3):
    sum_of_squares = s1**2 + s2**2
    
    if sum_of_squares < s3**2:
        return "Obtuse-angled"
    elif sum_of_squares == s3**2:
        return "Right-angled"
    else:
        return "Acute-angled"

side_a = eval(input("Enter length of side a: "))
side_b = eval(input("Enter length of side b: "))
side_c = eval(input("Enter length of side c: "))

triangle_type = type_triangle(side_a, side_b, side_c)
print(f"The triangle is ",triangle_type)