<?php

	if ($_POST['upload'] )

	 {

	   move_uploaded_file($_FILES["file"]["tmp_name"],
      "upload/" . $_FILES["file"]["name"]);

       // echo "Upload: " . $_FILES["file"]["name"] . "<br>";

       // echo "Type: " . $_FILES["file"]["type"] . "<br>";

       // echo "Size: " . ($_FILES["file"]["size"] / 1024) . " kB<br>";

       $var = "upload/" . $_FILES["file"]["name"];

       // echo "Stored in: " . $var."<br>";

       // $command = escapeshellcmd("python ./python_temp.py $var");
       // $command = escapeshellcmd("python ./resume_parsing.py $var");

			 // $command = escapeshellcmd("python ./parsing.py -p $var");
			 $command = escapeshellcmd("python ./parsing.py -p $var");

       // echo shell_exec($command);

       exec($command, $output, $ret_code)."<br";
       // echo "Return Code " . $ret_code;
			 // echo 'Values';
       // echo $output;
			 // print_r($output).'<br>';
			 echo '<pre>'; print_r($output); echo '</pre>';
			 // echo gettype($output)."<br";
			 // echo $output[0]."<br";
			 if (!empty($output))
			 {
				 $test = [];
				 $name = "";
				 $curr_company = "";
				 $curr_designation = "";
				 $curr_location = "";
				 $curr_email = "";
				 $skills = "";
				 $github = "";
				 $insta = "";
				 $linkedin = "";
				 $carobj = "";

				 echo '<br>';
				foreach($output as $key => $out) {
				    $test[$key] = json_decode($out, true);
						if(!empty($test[$key]['B-PERSON']))
							$name = $test[$key]['B-PERSON'];
						if(!empty($test[$key]['B-CURR-COMPANY']))
							$curr_company = $test[$key]['B-CURR-COMPANY'];
						if(!empty($test[$key]['B-CURR-DESIGNATION']))
							$curr_designation = $test[$key]['B-CURR-DESIGNATION'];
						if(!empty($test[$key]['B-CURR-LOCATION']))
			 				$curr_location = $test[$key]['B-CURR-LOCATION'];
						if(!empty($test[$key]['B-EMAIL']))
			 				$curr_email = $test[$key]['B-EMAIL'];
						if(!empty($test[$key]['B-SKILLS']))
							$b_skills = array_values($test[$key]['B-SKILLS']);
						if(!empty($test[$key]['B-GITHUB']))
							$github = $test[$key]['B-GITHUB'];
						if(!empty($test[$key]['B-INSTAGRAM']))
							$insta = $test[$key]['B-INSTAGRAM'];
						if(!empty($test[$key]['B-TWITTER']))
							$twitter = $test[$key]['B-TWITTER'];
						if(!empty($test[$key]['B-LINKEDIN']))
							$linkedin = $test[$key]['B-LINKEDIN'];
						if(!empty($test[$key]['B-CAR-OBJ']))
							$carobj = array_values($test[$key]['B-CAR-OBJ']);
						if(!empty($test[$key]['B-PROJECT-EXP']))
							$bprojectexp = array_values($test[$key]['B-PROJECT-EXP']);

				}
				echo '<br><br>';
				print_r($test);
				echo '<br>';
				print_r($test[$key]);
				echo '<b>';print_r("NAME : ".$name);echo '</b><br>';
				echo '<b>';print_r("CURRENT COMPANY : ".$curr_company);echo '</b><br>';
				echo '<b>';print_r("CURRENT DESIGNATION : ".$curr_designation);echo '</b><br>';
				echo '<b>';print_r("LOCATION : ".$curr_location);echo '</b><br>';
				echo '<b>';print_r("EMAIL : ".$curr_email);echo '</b><br>';
				echo '<b>';print_r("SKILLS : ".$b_skills[0]);echo '</b><br>';
				echo '<b>';print_r("GITHUB : ".$github);echo '</b><br>';
				echo '<b>';print_r("INSTA : ".$insta);echo '</b><br>';
				echo '<b>';print_r("LINKEDIN : ".$linkedin);echo '</b><br>';
				echo '<b>';print_r("Carrer : ");echo '</b><br>';
				foreach($carobj[0] as $value){
				    echo $value . "<br>";
				}
				echo '<b>';print_r("Project Exp : ");echo '</b><br>';
				echo '<b>';print_r("Count of Project Exp : ".count($bprojectexp));echo '</b><br>';
				foreach($bprojectexp[0] as $value){
				    echo $value . "<br>";
				}

				if(count($bprojectexp)> 0){

					foreach(count($bprojectexp) as $value){
						foreach($bprojectexp[$value] as $data){
							echo $data. "<br>";
						}
					}

				}

			}
       // echo $ret_code;
       // echo $output;

       #echo shell_exec("python python_temp.py");

     }

?>
