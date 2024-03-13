<h1>python-challenge</h1>

<h2>PyBank</h2>
<ul>
<li>Each row, not counting the header, is tallied up to get the total number of months.</li>
<li>The profit/loss amounts in the second column are also tallied to get the net amount over the period.</li>
<li>I attempted to tally up the change amounts from row to row, then divide them by the number of months to get the average change amount. However, I could't get the same amount as the intended result shown on the challenge page.</li>
<li>The greatest increase and decrease are tracked using the same method I used in the VBA challenge.</li>
<li>The results are then written into a .csv file and then exported to the analysis folder, then printed to the terminal.</li>
</ul>
<h2>PyPoll</h2>
<ul>
<li>Each row, not counting the header is tallied up to get the total number of votes.</li>
<li>The names of each candidate are stored in a list. Their own total amount of votes are stored in a separate list.</li>
<li>If the candidate isn't found in the list, it is added. If it is found, the list is put through a for loop to find the candidate matching the row in the file, then their vote count is tallied up.</li>
<li>The candidates' percentage is found using a function that divides the candidates' count by the total.</li>
<li>The winning candidate is found using the sme method to find the greatest increase in PyBank.</li>
<li>The results are written into a file, then printed to the terminal. A for loop is used to print the candidates' total and percentage.</li>
</ul>

For both parts of the module, I had help from GeeksForGeeks and my classmates.
