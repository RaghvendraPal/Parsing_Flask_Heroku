<!DOCTYPE html>
<html lang="en">

<head>
  <title>Resume Sample </title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link href='http://fonts.googleapis.com/css?family=Open+Sans:400,300,700' rel='stylesheet' type='text/css'>
  <link href="css/bootstrap.min.css" rel="stylesheet">
  <link rel="stylesheet" href="./fonts/font-awesome/font-awesome-4.7.0/css/font-awesome.min.css">
  <link href="css/styles.css" rel="stylesheet">

    <style>
        .pl{
            padding-left: 30px;
        }
        .work-experience{
            padding-left: 55px;
            margin-bottom: 40px;
        }
        .interest{
            padding-left: 65px;
            margin-bottom: 40px;
        }
        .skills {
            padding-left: 55px;
            margin-bottom: 40px;
        }
        .profile-infos {
            padding-left:50px;
            margin-bottom: 45px;
            padding-top: 30px;
        }
        .cd-container {
            width: 90%;
            max-width: 1170px;
            margin: 0 auto;
        }
        .cd-container::after {
            content: '';
            display: table;
            clear: both;
        }

        .cd-timeline {
            position: relative;
            padding: 2em 0;
            margin-top: 2em;
            margin-bottom: 2em;
        }
        .cd-timeline::before {
            content: '';
            position: absolute;
            top: 0;
            left: 18px;
            height: 100%;
            width: 4px;
            background: #d7e4ed;
        }
        @media only screen and (min-width: 1170px) {
            .cd-timeline {
                margin-top: 7em;
                margin-bottom: 3em;
            }
            .cd-timeline::before {
                left: 50%;
                margin-left: -2px;
            }
        }

        .cd-timeline-block {
            position: relative;
            margin: 2em 0;
        }
        .cd-timeline-block::after {
            clear: both;
            content: "";
            display: table;
        }
        .cd-timeline-block:first-child {
            margin-top: 0;
        }
        .cd-timeline-block:last-child {
            margin-bottom: 0;
        }
        @media only screen and (min-width: 1170px) {
            .cd-timeline-block {
                margin: 4em 0;
            }
            .cd-timeline-block:first-child {
                margin-top: 0;
            }
            .cd-timeline-block:last-child {
                margin-bottom: 0;
            }
        }

        .cd-timeline-img {
            position: absolute;
            top: 0;
            left: 0;
            width: 40px;
            height: 40px;
            border-radius: 50%;
            box-shadow: 0 0 0 4px #ffffff, inset 0 2px 0 rgba(0, 0, 0, 0.08), 0 3px 0 4px rgba(0, 0, 0, 0.05);
        }
        .cd-timeline-img img {
            display: block;
            width: 24px;
            height: 24px;
            position: relative;
            left: 50%;
            top: 50%;
            margin-left: -12px;
            margin-top: -12px;
        }
        .cd-timeline-img.cd-picture {
            background: #ffffff;
            text-align: center;
            padding-top: 18px;
            font-size: 25px;
            color: #3b658a;;
        }
        @media only screen and (min-width: 1170px) {
            .cd-timeline-img {
                width: 60px;
                height: 60px;
                left: 50%;
                margin-left: -30px;
                -webkit-transform: translateZ(0);
                -webkit-backface-visibility: hidden;
            }
        }

        .cd-timeline-content {
            position: relative;
            margin-left: 60px;
            background: #fff;
            border-radius: 0.25em;
            padding: 1em;
            border-left: 1px solid #3b658a;
            box-shadow: 0 3px 6px rgba(132, 131, 131, 0.16), 0 3px 6px rgba(117, 117, 117, 0.23);
        }
        .cd-timeline-content::after {
            clear: both;
            content: "";
            display: table;
        }
        .cd-timeline-content h2 {
            color: #303e49;
        }


        .cd-timeline-content p {
            margin: 1em 0;
            line-height: 1.6;
        }

        .cd-timeline-content .cd-date {
            float: left;
            padding: .8em 0;
            opacity: .7;
        }
        .cd-timeline-content::before {
            content: '';
            position: absolute;
            top: 16px;
            right: 100%;
            height: 0;
            width: 0;
            border: 7px solid transparent;
            border-right: 7px solid #ffffff;
        }
        @media only screen and (min-width: 768px) {
            .cd-timeline-content h2 {
                font-size: 20px;
            }
            .cd-timeline-content p {
                font-size: 15px;
            }
        }
        @media only screen and (min-width: 1170px) {
            .cd-timeline-content {
                margin-left: 0;
                padding: 1.6em;
                width: 45%;
            }
            .cd-timeline-content::before {
                top: 24px;
                left: 100%;
                border-color: transparent;
                border-left-color: #3b658a;
            }

            .cd-timeline-content .cd-date {
                position: absolute;
                width: 100%;
                left: 125%;
                top: 0px;
                font-size: 25px;
            }

            .cd-timeline-block:nth-child(even) .cd-timeline-content {
                float: right;
            }

            .cd-timeline-block:nth-child(even) .cd-timeline-content::before {
                top: 24px;
                left: auto;
                right: 100%;
                border-color: transparent;
                border-right-color: #3b658a;
            }

            .cd-timeline-block:nth-child(even) .cd-timeline-content .cd-date {
                left: auto;
                right: 125%;
                text-align: right;
            }
        }

    </style>

</head>

<body >
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
     // echo '<pre>'; print_r($output); echo '</pre>';
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
    //   echo '<br><br>';
    //   print_r($test);
    //   echo '<br>';
    //   print_r($test[$key]);
    //   echo '<b>';print_r("NAME : ".$name);echo '</b><br>';
    //   echo '<b>';print_r("CURRENT COMPANY : ".$curr_company);echo '</b><br>';
    //   echo '<b>';print_r("CURRENT DESIGNATION : ".$curr_designation);echo '</b><br>';
    //   echo '<b>';print_r("LOCATION : ".$curr_location);echo '</b><br>';
    //   echo '<b>';print_r("EMAIL : ".$curr_email);echo '</b><br>';
    //   echo '<b>';print_r("SKILLS : ".$b_skills[0]);echo '</b><br>';
    //   echo '<b>';print_r("GITHUB : ".$github);echo '</b><br>';
    //   echo '<b>';print_r("INSTA : ".$insta);echo '</b><br>';
    //   echo '<b>';print_r("LINKEDIN : ".$linkedin);echo '</b><br>';
    //   echo '<b>';print_r("Carrer : ");echo '</b><br>';
    //   foreach($carobj[0] as $value){
    //     echo $value . "<br>";
    // }
    // echo '<b>';print_r("Project Exp : ");echo '</b><br>';
    // echo '<b>';print_r("Count of Project Exp : ".count($bprojectexp));echo '</b><br>';
    // foreach($bprojectexp[0] as $value){
    //     echo $value . "<br>";
    // }

     // echo $ret_code;
     // echo $output;

     #echo shell_exec("python python_temp.py");

   }
 }

 ?>
<section id="content-body" class="container animated">
  <div class="row">

    <!-- Header Colors -->
    <div class="col-md-10 col-sm-10  col-md-offset-2 col-sm-offset-1 clearfix top-colors">
      <div class="top-color top-color1"></div>
      <div class="top-color top-color2"></div>
      <div class="top-color top-color3"></div>
      <div class="top-color top-color1"></div>
      <div class="top-color top-color2"></div>
    </div>

    <!-- Beginning of Content -->
    <div class="col-md-10 col-sm-10 col-md-offset-2 col-sm-offset-1 resume-container">


      <div class="profile-intro row">

        <div class="col-md-4 profile-col">
          <div class="profile-pic">
            <div class="profile-border">
              <img src="img/avatar.jpg" alt="">
            </div>
          </div>
        </div>

        <div class="col-md-7">
          <h1 class="intro-title1">Hi, i'm <span class="color1 bold"><?php echo explode(" ", $name)[0]; ?></span></h1>
            <h2 class="intro-title2"><?php echo $curr_designation ?></h2>
            <p>
                <?php
                    foreach($carobj[0] as $value){
                      echo $value ;
                    }
                ?>
            </p>
        </div>

      </div>

      <div class="timeline-wrap">
        <div class="timeline-bg">

          <!--   SECTION: PROFILE INFOS  -->
          <section class="timeline profile-infos">
                    <h2 class="section-title">Profile</h2>
              <div class="line row">
                  <div class="col-md-8 content-wrap bg1">
                         <div class="line-content">
                             <h3 class="section-item-title-1">FULL NAME</h3>
                             <p><?php echo $name ?></p>
                         </div>
                    </div>
            </div>
              <div class="line row">
                  <div class="col-md-8 content-wrap bg1">
                    <div class="line-content">
                      <h3 class="section-item-title-1">Email</h3>
                        <p><?php echo $curr_email ?></p>
                    </div>
              </div>

            </div>

            <div class="line row">
                 <div class="col-md-8 content-wrap bg1">
                <div class="line-content">
                  <!-- Subtitle -->
                  <h3 class="section-item-title-1">Find Me On</h3>
                  <a href="#" class="btn btn-default"><i class="fa fa-facebook"></i></a>
                  <a href="'<?php $twitter?>'" class="btn btn-default"><i class="fa fa-twitter"></i></a>
                  <a href="'<?php $linkedin?>'" class="btn btn-default"><i class="fa fa-linkedin"></i></a>
                  <a href="#" class="btn btn-default"><i class="fa fa-link"></i></a>
                  <!-- /Content -->
                </div>
              </div>
              <div class="col-md-1 bg1 timeline-space full-height hidden-sm hidden-xs"></div>
            </div>
          </section>


          <!--EDUCATION-->
            <div class="col-md-8">
                <h2 class="section-title pl">Education</h2>
            </div>
            <section id="cd-timeline" class="cd-timeline cd-container">
                <div class="cd-timeline-block">
                    <div class="cd-timeline-img cd-picture">
                        <i class="fa fa-graduation-cap"></i>
                    </div>

                    <div class="cd-timeline-content">
                        <h2>Title of section 1</h2>
                        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Iusto, optio, dolorum provident rerum aut hic quasi placeat iure tempora laudantium ipsa ad debitis unde? Iste voluptatibus minus veritatis qui ut.</p>
                        <span class="cd-date">Jan 14</span>
                    </div>
                </div>

                <div class="cd-timeline-block">
                    <div class="cd-timeline-img cd-picture">
                        <i class="fa fa-graduation-cap"></i>
                    </div>

                    <div class="cd-timeline-content">
                        <h2>Title of section 2</h2>
                        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Iusto, optio, dolorum provident rerum aut hic quasi placeat iure tempora laudantium ipsa ad debitis unde?</p>
                        <span class="cd-date">Jan 18</span>
                    </div>
                </div>

                <div class="cd-timeline-block">
                    <div class="cd-timeline-img cd-picture">
                        <i class="fa fa-graduation-cap"></i>
                    </div>

                    <div class="cd-timeline-content">
                        <h2>Title of section 3</h2>
                        <p>Lorem ipsum dolor  error assumenda quae quasi repudiandae sed quod veniam dolore possimus rem voluptatum eveniet eligendi quis fugiat aliquam sunt similique aut adipisci.</p>
                        <span class="cd-date">Jan 24</span>
                    </div>
                </div>

                <div class="cd-timeline-block">
                    <div class="cd-timeline-img cd-picture">
                        <i class="fa fa-graduation-cap"></i>
                    </div>

                    <div class="cd-timeline-content">
                        <h2>Title of section 4</h2>
                        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Iusto, optio, dolorum provident rerum aut hic quasi placeat iure tempora laudantium ipsa ad debitis unde? Iste voluptatibus minus veritatis qui ut.</p>
                        <span class="cd-date">Feb 14</span>
                    </div> <!-- cd-timeline-content -->
                </div>

            </section>



          <!--EXPERIENCE-->
            <section class="timeline work-experience">
                <div class="line row">
                    <div class="col-md-11 content-wrap bg1">
                        <!-- Section title -->
                        <h2 class="section-title">Work Experience</h2>
                    </div>
                </div>

                <?php

                  for($i = 0; $i < count($bprojectexp); $i++){
                ?>
                  <div class="line row">
                      <div class="col-md-11 content-wrap bg1">
                          <div class="line-content line-content-education">
                              <!-- Work Place -->
                              <h3 class="section-item-title-1">Oasis Ltda.</h3>

                              <h4 class="job"><i class="fa fa-flag"></i> Front-end Developer - <span class="job-date">Jan 2010 - Apr 2012</span></h4>

                              <div class="job-description">
                                  <p>
                                  <?php
                                    foreach($bprojectexp[$i] as $value){
                                      echo $value. "<br>";
                                    }
                                  ?>
                                </p>
                              </div>
                          </div>
                      </div>
                  </div>
                  <!-- /SECTION ITEM -->
                <?php
                }
                ?>
            </section>

          <!--SKILLS-->
          <section class="timeline skills"  >
                <div class="line row">
                  <div class="col-md-8 content-wrap bg1">
                    <!-- Section title -->
                    <h2 class="section-title">Skills</h2>
                  </div>
                </div>

                <div class="line row">
                    <h3 class="col-md-11 section-item-title-1">Professional Skills</h3>

                    <div class="col-md-8 content-wrap bg1">
                    <div class="line-content">
                        <ul class="skills-list">
                        <li>
                          <div class="progress">
                            <div class="progress-bar" role="progressbar" data-percent="70%" style="width: 70%;">
                                <span class="sr-only">70% Complete</span>
                            </div>
                            <span class="progress-type">Comunication</span>
                            <span class="progress-completed">70%</span>
                          </div>
                        </li>

                        <li>
                          <div class="progress">
                            <div class="progress-bar progress-bar-2" role="progressbar" data-percent="90%" style="width: 90%;">
                                <span class="sr-only">90% Complete</span>
                            </div>
                            <span class="progress-type">Leadership</span>
                            <span class="progress-completed">90%</span>
                          </div>
                        </li>

                        <li>
                          <div class="progress" title="Doing my best!">
                            <div class="progress-bar progress-bar-3" role="progressbar" data-percent="85%" style="width: 85%;">
                                <span class="sr-only">85% Complete</span>
                            </div>
                            <span class="progress-type">Confidence</span>
                            <span class="progress-completed">85%</span>
                          </div>
                        </li>
                        <!-- /item list -->
                      </ul>
                      <!-- /Content -->
                    </div>
                  </div>

                </div>

                <div class="line row">
                    <h3 class="col-md-11 section-item-title-1">Software Skills</h3>
                    <div class="col-md-8 content-wrap bg1">
                    <div class="line-content">
                      <!-- Subtitle -->

                      <ul class="skills-list">
                        <!-- item-list -->
                        <li>
                          <div class="progress">
                            <div class="progress-bar" data-percent="85%" role="progressbar" style="width: 85%;">
                                <span class="sr-only">85% Complete</span>
                            </div>
                            <span class="progress-type"><?php echo $b_skills[0] ?></span>
                            <span class="progress-completed">85%</span>
                          </div>
                        </li>

                        <li>
                          <div class="progress">
                            <div class="progress-bar progress-bar-2" data-percent="90%" role="progressbar" style="width: 90%;">
                                <span class="sr-only">90% Complete</span>
                            </div>
                            <span class="progress-type"><?php echo $b_skills[1] ?></span>
                            <span class="progress-completed">90%</span>
                          </div>
                        </li>

                        <li>
                          <div class="progress">
                            <div class="progress-bar progress-bar-3" data-percent="40%" role="progressbar" style="width: 40%;">
                                <span class="sr-only">40% Complete</span>
                            </div>
                            <span class="progress-type"><?php echo $b_skills[2] ?></span>
                            <span class="progress-completed">40%</span>
                          </div>
                        </li>
                        <!-- /item list -->
                      </ul>
                      <!-- /Content -->
                    </div>
                  </div>
                </div>

                <div class="line row">
                    <h3 class="col-md-11 section-item-title-1">Code Skills</h3>

                    <div class="col-md-8 content-wrap bg1">
                <div class="line-content">
                  <!-- Subtitle -->

                  <ul class="skills-list">
                    <!-- item-list -->
                    <?php
                      for ($i = 0; $i < count($b_skills); $i++){
                    ?>
                    <li>
                      <div class="progress">
                        <div class="progress-bar" data-percent="90%" role="progressbar" style="width: 90%;">
                            <span class="sr-only">90% Complete</span>
                        </div>
                        <span class="progress-type"><?php echo $b_skills[$i] ?></span>
                        <span class="progress-completed">90%</span>
                      </div>
                    </li>
                    <?php
                      }
                    ?>

                    <!-- /item list -->
                  </ul>
                  <!-- /Content -->
                </div>
              </div>
             </div>
          </section>

          <!--INTEREST-->
          <section class="timeline interest" >

            <div class="line row">
              <div class="col-md-12 content-wrap bg1">
                  <h2 class="section-title">Interests</h2>
              </div>
            </div>

            <div class="line row">
              <div class="col-md-12 content-wrap bg1">
                <div class="line-content">
                  <h3 class="section-item-title-1">Art</h3>

                  <p>Praesent tellus ligula,tinciduntet fringilla vel, tincidunt ut dui. Nulla feugiat, lacus ac malesuada lobortis, elit nunc congue nunc, vel imperdiet lorem leo a lectus.</p>
                </div>
              </div>
            </div>

            <div class="line row">
                <div class="col-md-12 content-wrap bg1">
                <div class="line-content">
                  <!-- Subtitle -->
                  <h3 class="section-item-title-1">Games</h3>

                  <p>Praesent tellus ligula, tincidunt et fringilla vel, tincidunt ut dui. Nulla feugiat, lacus ac malesuada lobortis, elit nunc congue nunc, vel imperdiet lorem leo a lectus.</p>
                </div>
              </div>
            </div>

            <div class="line row">
                <div class="col-md-12 content-wrap bg1">
                <div class="line-content">
                  <!-- Subtitle -->
                  <h3 class="section-item-title-1">Books</h3>

                  <p>Praesent tellus ligula, tincidunt et fringilla vel, tincidunt ut dui. Nulla feugiat, lacus ac malesuada lobortis, elit nunc congue nunc, vel imperdiet lorem leo a lectus.</p>
                  <!-- /Content -->
                </div>
              </div>
            </div>
          </section>


          <!-- SECTION: THANK YOU  -->
          <section class="timeline profile-infos">

            <!-- SECTION ITEM -->
            <div class="line row line-thank-you">

              <div class="col-md-2"></div>

              <div class="col-md-8 content-wrap bg1">
                <div class="line-content">

                  <h3 class="thank-you">Thank You!</h3>

                </div>
              </div>

              <div class="col-md-2 bg1"></div>

            </div>
          </section>
        </div>
      </div>

      <!-- ============  FOOTER ================= -->
      <footer id="footer" class="row">

        <p class="quote">“Ideas are the beginning points of all fortunes”</p>

        <p class="author">Napoleon Hill</p>

      </footer>
    </div>
  </div>
</section>

</body>

</html>
