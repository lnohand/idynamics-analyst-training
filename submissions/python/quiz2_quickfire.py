import pandas as pd

BOOKS = "assignments/python/quiz2_data/books.csv"
LOANS = "assignments/python/quiz2_data/loans.csv"

books = pd.read_csv(BOOKS)
loans = pd.read_csv(LOANS)

print("Question 1:")
book_count = books["book_id"].count()
page_count = books["pages"].sum()
loan_count = loans["loan_id"].count()
print(f"Books:  {book_count}")
print(f"Pages: {page_count:,}")
print(f"Loans: {loan_count}")

print("Question 2:")
later = books[(books["year"] >= 2015) & (books["price"] < 20)]
later = books.sort_values("price", ascending=False)
print(later[["title", "year", "price"]].to_string(index=False))

print("Question 3:")
piz = books.groupby("category", as_index=False)["pages"].sum()
piz = piz.sort_values("pages", ascending=False)
print(piz.to_string(index=False))
piz = piz[(piz["pages"] >= 1000)]
print()
print(piz.to_string(index=False))

print("Question 4:")
books["hours"] = round(books["pages"] / 40, 1)
longer = books[(books["hours"] >= 10)]
longer = longer.sort_values("hours", ascending=False)
print(longer[["title", "hours"]].to_string(index=False))

print("Question 5:")
average = books["price"].mean()
print(f"Average price: ${average:,.2f}")
books["vs_average"] = round(books["price"] - average,2)
below = books[(books["vs_average"] < 0)]
print(f"Below average: {below["book_id"].count()}")

print("Question 6:")
loaned = loans.groupby("book_id", as_index=False)["days"].sum()
print(loaned)
piz = pd.merge(books[["book_id", "title"]], loaned, on="book_id", indicator=True)
piz = piz.fillna(0)
piz = piz.sort_values("days", ascending=False)
piz = piz[(piz["days"] >= 30)]
print(piz[["title", "days"]].to_string(index=False))

print("Question 7:")
both = pd.merge(books[["book_id", "title"]], loaned, how="outer", on="book_id", indicator=True)
never = both[both["_merge"] == "left_only"]
never = never.fillna(0)
no_id = both[both["_merge"] == "right_only"]
print(never[["book_id", "title", "days"]].to_string(index=False))
print(no_id[["book_id", "days"]].to_string(index=False))

print("Question 8:")
def category_stats(table, category):
    books_category = books[books["category"] == category]
    return {
        "category": category,
        "books": len("books_category"),
        "pages": books_category["pages"].sum(),
        "average": round(books_category["pages"].mean(),1)
    }

books_row = []
for genre in ["Fiction", "Cooking", "Science"]:
    books_row.append(category_stats(books, genre))
    
books_table = pd.DataFrame(books_row)
print(books_table.to_string(index=False))
books_table.to_csv("submissions/python/quiz2_categories.csv", index=False)
print("Saved submissions/python/quiz2_categories.csv")

print("Question 9:")
print("a) This will print the total pages in each category of the books table with an index on the left side. It will then print the total pages in the Fiction category. Category is the index here.")
print("b) This will not run because the Fiction column no longer exists. Due to the lack of an index column, Python treats by_cat as a table meaning that to determine the total number of pages from the Fiction category, you must run the following line: print(by_cat[by_cat[""category""] == ""Fiction""]). Remove the extra quotations to make it work.")
print("c) The category will no longer show up and it will be a list of the page sums. I believe b) is better because it is simple to read and parsing the information from it requires using the usual table logic. ")
print("d) The numbers on the left count the number of entries. It is not a column I believe. It does not have an index.")