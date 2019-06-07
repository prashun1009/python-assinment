For the given program, we will be passing the two files as command line arguments


1. We take first argument as first file and second as second file.
2. We create two dictionary urlh1 nd urlh2 in which we store urlh from the files as key and available_price as value.
3. We create two lists as cat1 and cat2 to get unique categories and check if category is not already present in the lists then we add it to the list else we ignore it.
4. We match the key present in urlh1 with urlh2 and if found in urlh2, it is overlapping we increase the count and we take the difference of the values, i.e., available_price.
5. Cat1 and Cat2 have unique categories from file 1 and file 2.
6. To get unique categories from both files, we are checking if items present in cat1 are not in cat 2 and items present in cat2 are not in cat1 then we append it to a new list unqiue_cat.
7. To create taxonomy we took all subcategories in sub1 and sub2 for file1 and file2 then count unique and count frequency of each subcategory in the list and matched them with dictionary of category and subcategory stored in t_cat1 and t_cat2 for file1 and file2.
8. For mrp normalization, we read file line by line and check if mrp is 0 we change it to "NA" and write the lines to a new file.