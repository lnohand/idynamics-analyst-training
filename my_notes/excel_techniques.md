1. Actuals is the place where you enter the data and then it is implemented into the rest of the excel sheets. This was created to centralize the point of data entry into one sheet. Prior to the creation of this sheet, the same number existed in 3 separate location. This simplifies checking for mistakes as it should all be traceable to one location.

2. The config cell details what the current month is, what the previous month was, and the final day of the current month. This was created to simplify month specific 
information and make 2 cells control the current month so 1 input can change an entire sheet and prevent forgetting a input and ruining everything. Essentially, any formula that needs to know the current or previous month will be referencing the config cells from now on. The limitations are that there's only 1 config per tab, retention will need to be extended as we increase the amount of months, and I3 is a text string.

3. Instead of referencing a specific column like in the current Retention tab, the new lookup format uses the index match function to dynamically look at the new
GRR and NRR values and update them. It is created by referencing the final day in the config cell and finding it in row 4 then returning the value in the same position in row 6. 

4. I used the Indirect function which takes a text string and converts it into a cell reference. This is used when a cell needs to be referenced but the name is stored in a different cell and changes. This should not be used when it can be replaced with an index match. 

5. The text concatenation references the SaaS KPIs then finds the specific values (the Closing MRR, NRR, and EBITDA Margin) and separates each section of text and numbers with an &. 

6. Step 1: Enter the actuals in the Actuals Tab. Step 2: Update the Retention Tab. Step 3: Duplicate the prior month's tab. Step 4: Update the two config cells in the new tab. 