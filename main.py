"""
What you should know: Store and access collections of items.
Practice Prompt: Make a list of 5 sewing projects
and use a loop to print them with numbers (like a ranked list).
"""

"""--------------Initial Code-----------------"""
sewing_projects = ["hat","shirt","pants","skirt","dress"]

for item in sewing_projects:
    index_number = sewing_projects.index(item) + 1
    print(f"{index_number}.{item}")
"""--------------How to Improve Code-----------------
1. .index(item) searches the list from the beginning each time
this means the code isn't as efficient as it should be.
2.If there are duplicates in the list, .index() will return
the first occurrence so the numbering could be wrong.
----notes------

*enumerate(sewing_projects, start=1) gives back each project with a number.
ex: (1, "hat"), (2, "shirt"), (3, "pants")
*The loop takes each pair, i is the number (1, 2, 3, …).
*project is the actual name ("hat", "shirt")
"""
"""--------------------Final Code-------------------"""
sewing_projects = ["hat","shirt","pants","skirt","dress"]
for i, project in enumerate(sewing_projects, start=1):
    print(f"{i}. {project}")


