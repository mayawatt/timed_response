This was a project done at the Montreal Computational and Quantitative Linguistics Lab at McGill University and presented at CogSci 2021.

Here is a link to the poster presentation: https://aaa.underline.io/lecture/27386-processing-differences-among-irregular-inflection-classes

The project involved developing an online experiment using jsPsych. The webpage diplayed various stimuli and collected data on participants reaction times. This data was hosted on Google Firebase, and the data was analysed in R with the help of Mika Bradinsky at MIT.

CREATING THE EXPERIMENT I hosted the experiment on GitHub pages and stored participants' data on Google Firebase’s Realtime Database. This combination works well -- the GitHub desktop app makes updating the experiment very easy, and Firebase’s Realtime Database makes participants’ data available immediately. Ideally, the data collection and hosting would be on the same website -- JsPsych provides documentation for this (see ‘Data Storage, Aggregation and Manipulation’). However, all implementations include writing a PHP file, which GitHub doesn’t support. It’s possible to do both hosting and data collection on Firebase (see this person’s implementation: https://github.com/napulen/melodictension), but I found the combination of GitHub and Firebase fairly straightforward, so I went with that instead.

GITHUB PAGES I used GitHub Pages to host the experiment. See https://pages.github.com/ for instructions on how to do this.

FIREBASE SETUP AND INSTALLATION In order to use Firebase, I did the following in-order:

(1) Login to https://firebase.google.com/ with a Google account and create a “New Project”.
(2) Open the terminal and cd to the root directory (cd /). Install Node.js (I did so via Homebrew). This installs npm.
(3) Run npm install -g firebase-tools in the terminal to install the Firebase CLI (Command Line Interface).
(4) Save your project in a directory within a directory and cd into the outer directory. I had my index.html in a folder in a folder on my desktop.
(5) Log into the CLI. You do this with the command firebase login. You will be asked to login with your Google username and password. My terminal didn’t recognize firebase, so I copy-pasted the following alias into my terminal: npm config get prefix/bin/firebase
(6) Run firebase init. When asked which CLI features you’d like to set up, choose "Database".* You’ll be asked to set up a default project for the directory. Select the inner folder (i.e. the folder with your project).
(7) Hit enter twice to select the default options for the next two questions, then enter "N" for the third. Finally, hit enter again to accept the default name for your storage rules. *At first, firebase init gave an error saying firebase.auth() is not a function. This seems to be a common problem. I fixed it using this person’s documentation: https://stackoverflow.com/questions/48592656/firebase-auth-is-not-a-function I stopped following the documentation after deploying (I think I may have tried it and it just didn’t work for me). Instead I followed this tutorial, which I highly recommend: https://www.youtube.com/watch?v=noB98K6A0TY Firebase’s free real time database stores 1 GB of data. Each experiment takes up 294.6 KB of data. Firebase can accommodate the data for 3,394 participants.

INTEGRATING WITH MECHANICAL TURK I saved the data in CSV format (using one of the JsPsych plug-ins). I’m sure there’s a more elegant solution to make the data compatible with Firebase, but this worked fine.

CHANGES TO THE SAME-DIFFERENT-HTML PLUGIN The first_stim_duration and second_stim_duration weren’t working (they were stuck on default), so I went into the plugin and changed the defaults to the durations I wanted (1000ms for first_stim_duration and null for second_stim_duration, which is an indefinite amount of time). I also changed the blank screen gap between the stimuli to 0. These changes made the stimuli and prompt display a lot nicer and smoother.

RESOURCES Responding to Non-Words in the Lexical Decision Task: Insights from the Lexical English Project https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4404174/pdf/nihms626380.pdf The past tense inflection project (PTIP): speeded past tense inflections, imageability ratings, and past tense consistency measures for 2,200 verbs https://link.springer.com/c
