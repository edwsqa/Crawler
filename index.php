#<?php
#header("Location: http://files-scraper.rahtiapp.fi/files ");
#exit();
#?>

<?php
echo "<html><body><table>\n\n";
$f = fopen("jimms.csv", "r");
while (($line = fgetcsv($f)) !== false) {
        echo "<tr>";
        foreach ($line as $cell) {
                echo "<td>" . htmlspecialchars($cell) . "</td>";
        }
        echo "</tr>\n";
}
fclose($f);
echo "\n</table></body></html>";
