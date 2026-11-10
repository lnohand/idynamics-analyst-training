import pandas as pd

COURSES= "assignments/python/quiz3_data/courses.csv"
ENROLLMENTS = "assignments/python/quiz3_data/enrollments.csv"
INSTRUCTORS = "assignments/python/quiz3_data/instructors.csv"

courses = pd.read_csv(COURSES)
enrollments = pd.read_csv(ENROLLMENTS)
instructors = pd.read_csv(INSTRUCTORS)

print("Question 1:")
print(f"Courses: {courses["course_id"].count()}")
print(f"Instructors: {instructors["instructor_id"].count()}")
print(f"Enrollments: {enrollments["enroll_id"].count()}")
print(f"Total paid: ${enrollments["paid"].sum()}")

print()
print("Question 2:")
chiz = courses[(courses["price"] >= 50) & (courses["price"] < 80)]
chiz.sort_values("price", ascending=False)
print(chiz[["title", "category", "price"]].to_string(index=False))

print()
print("Question 3:")
dul = enrollments.groupby("month", as_index=False)["paid"].sum()
dul = dul.sort_values("paid", ascending=False)
print(dul.to_string(index=False))

print()
print("Question 4:")
nihu = pd.merge(enrollments, courses, on="course_id", how="outer", indicator=True)
pizdu = nihu[nihu["_merge"] == "right_only"]
pizdu = pizdu.fillna(0)
nihu = nihu.groupby(["course_id", "title"], as_index=False)["paid"].sum()
nihu = nihu.fillna(0)
nihu = nihu.sort_values("paid", ascending=True)
print(nihu[["course_id", "title", "paid"]].to_string(index=False))
print("Courses with no sales:")
print(pizdu[["title", "course_id", "paid"]].to_string(index=False))

print()
print("Question 5:")
bru = pd.merge(enrollments, courses, on="course_id", how="left", indicator=True)
heh = bru.groupby(["month", "student", "title"], as_index=False)["paid"].sum()
heh = heh[heh["month"] == "2026-09"]
sept = enrollments[enrollments["month"] == "2026-09"]
print(heh.to_string(index=False))
print(f"Total in report: ${heh["paid"].sum()}")
print(f"Total paid in September: ${sept["paid"].sum()}")

print()
print("Question 6:")
never = pd.merge(instructors, courses, on="instructor_id", how="outer", indicator=True)
nev = never[never["_merge"] == "left_only"]
ev = never[never["_merge"] == "right_only"]
nev = nev.fillna(0)
print(nev[["instructor_id", "name"]].to_string(index=False))
print(ev[["course_id", "title", "instructor_id"]].to_string(index=False))

print()
print("Question 7:")
pay = instructors.merge(courses, on="instructor_id", how="left").merge(enrollments, on="course_id", how="left")
pay = pay.groupby("instructor_id", as_index=False)["paid"].sum()
pay = pay.fillna(0)
pay = pay.sort_values("paid", ascending=False)
print(pay.to_string(index=False))

print()
print("Question 8:")
def month_stats(table, month):
    enrollments_total = enrollments[enrollments["month"] == month]
    return {
        "month": month,
        "enrollments": len("enrollments_total"),
        "paid": enrollments_total["paid"].sum(),
        "avg_paid": round(enrollments_total["paid"].mean(),1)
    }

enrollments_row = []
for enroll in ["2026-07", "2026-08", "2026-09"]:
    enrollments_row.append(month_stats(enrollments, enroll))
    
enrollments_table = pd.DataFrame(enrollments_row)
print(enrollments_table.to_string(index=False))
enrollments_table.to_csv("submissions/python/quiz3_months.csv", index=False)
print("Saved submissions/python/quiz3_months.csv")