<?php
// you can add to the array
$ext_array = array(".htm", ".php", ".asp", ".js");
//list of extensions not required (above)
$dir1 = "."; 
$filecount1 = 0; 
$d1 = dir($dir1); 

while ($f1 = $d1->read()) { 
$fext = substr($f1,strrpos($f1,".")); //gets the file extension
if (in_array($fext, $ext_array)) { //check for file extension in list
continue;
}else{
if(($f1!= '.') && ($f1!= '..')) { 
if(!is_dir($f1)) $filecount1++;

$thelist .= '<LI><a href="'.$f1.'">'.$f1.'</a>';

} 
}
}

// add text and count number below files
echo "Total files in folder: ";
echo "$filecount1";
?>

<P>Dir:</p>
<UL>
<P><?=$thelist?></p>
</UL>
