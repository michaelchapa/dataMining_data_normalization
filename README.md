# dataMining_data_normalization
<h4>Develop a program for the pre-processing data.</h4>
<ol>
  <li>Read data from the provided CSV file into a DataFrame</li>
  <li>Data-file has 6 columns: A, B, C, D, E, F</li>
  <li>A & B are categorical and the rest are numeric</li>
</ol>

<h2>Data Statistics</h2>
<h3>Write functions to calculate columns C, D, E, F</h3>
<ol>
  <li>Mean & Midrange</li>
  <li>Mode & Modality (i.e., bimodal, trimodal, etc.)</li>
  <li>Five-number summary</li>
  <li>Compare to the corresponding functions provided by DataFrame</li>
</ol>

<h2>Similarity & Distance</h2>
<h3>Prompt the user for a tuple, p = (a1, b2, 515, -0.876, 6.4253, 45)</h3>
<h4>Using the set of columns C, D, E, F: Print row in DataFrame that is LEAST dissimilar to 'p'</h4>
<ol>
  <li>Euclidian distance</li>
  <li>Manhattan distance</li>
  <li>Supremum distance</li>
  <li>Cosine similarity</li>
</ol>

<h3>Normalize the data points by making the norm of each data point (under columns C, D, E, F) equal to 1. </h3>
<h3>Scale the values in columns C, D, E, F; so that for each row (C, D, E, F) we have: sqrt(C^2 + D^2 + E^2 + F^2) = 1.</h3>
<h3>Print the row in the DataFrame that has the shortest Euclidiean distances from the normalized point 'p'.</h3>

<h2>Normalization</h2>
<h3>Write/Apply functions to column C to normalize the data in a given column using the following methods:</h3>
<ol>
  <li>Min-Max normalization that transforms the values onto a given range, (EX [-1.0, 1.0]).</li>
  <li>Z-score normalization</li>
  <li>Decimal scaling normalization</li>
  
  
