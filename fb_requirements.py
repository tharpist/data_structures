"""
Facebook Requirements
Topic 1 Arrays and Strings

Relevant topics from the "Technical Screen Interview Guide" 

TOPIC 1 | ARRAYS & STRINGS

A Very Big Sum (Warm-up, learning how to use HackerRank)
Designer PDF Viewer
Left Rotation
TOPIC 3 | STACKS & QUEUES

Pre-work: If you need a refresher, take a look at this video
Exercises:
Balanced Brackets
Queue Using Two Stacks
TOPIC 4 | HASH & MAPS

Pre-work: If you need a refresher, take a look at this video
Exercises:
Ice Cream Parlor
Colorful Number (This one might be challenging. Remember, if you get stuck, refer to our proposed solution.)
TOPIC 6 | TREES

Theory: If you need a refresher, take a look at this video
Exercises:
QHeap1
TOPIC 7 | GRAPHS (BFS & DFS)

Theory: Watch this video to understand what a graph is and how to traverse it
Exercises:
Snakes and Ladders
 

------------------------------------------

General Interview Tips

Be open about what you know and don’t know. One of the goals is to find the limits of your knowledge and see how you react outside of that so always attempt to answer the question at hand. The interviewer will provide hints along the way if you get stuck.
Ask clarifying questions whenever necessary.
Think through your solutions out loud, and share as much relevant knowledge as possible.
Take hints from the interviewer and don’t be afraid to change your mind as you go.
Please make sure you are in a quiet place with a reliable internet connection.
 

Coding/Scripting Prep:

Coding Interview Environment

The coding is done 'live' via CoderPad (http://coderpad.io/), a collaborative document editor specifically designed for coding interviews.

Language Selection

As there are many different programming languages used at Facebook to solve infrastructure challenges, we don't have a preference for the language (or languages) you use during the interview. We think that if you can show us solid programming skills in one language, you'll be able to transfer them to other languages.

Types of Questions Asked

The questions we ask require skills used every day by Systems Engineers, including text manipulation, handling input/output, automating tasks, interfacing with external systems/processes, etc. The questions can be a real problem, or something contrived to use these skills.

 

Interview Tips:

Your primary goal in the interview is to obtain a working solution to each problem in a reasonable amount of time.
Make sure you are in a quiet place with a reliable internet connection. Headphones are very handy. A speakerphone also usually provides acceptable sound quality. Holding the phone in your neck for 45 minutes while you try and type is going to be a pain. Close your email and chat apps to avoid interruptions.
We will always paste in the text of any coding question we ask you. Take some time after reading the question to ask questions and plan out your solution, rather than jumping right into its implementation.
Defensive coding is important, but don't focus on details (such as error handling and corner cases) to the detriment of the overall solution. If you're not sure if a given error handling or edge case is important, ask the interviewer.
Don’t get hung up on syntax. If you can’t remember the order or arguments to a function or its name, just say so, leave a placeholder and move on.
While you don’t need to provide a play by play of your thought process throughout the interview, it’s best to let the interviewer know why you are making certain decisions, and do most of your work in the CoderPad window. This will also help with any course corrections that may be needed while you are solving the problem.
Take hints from the interviewer and be open to other solutions as you go. It's completely acceptable to present a rough solution in the beginning and iterate as you go along.
Use the language you are strongest in. Don't use a language you know less well because you think it will please the interviewer. If the interviewer doesn't know your strongest language, they will figure it out later.
Don’t be afraid to change your mind. If you think you’ve started your solution in the wrong way, or even in the wrong language, it’s OK to admit it and change tack (and the sooner you do it the better).
Resist the temptation to look things up on the internet during your interview. We'd rather have you get a function name incorrect or the order of arguments wrong than have you looking things up during the interview. We want to see you write code and think on your feet, not search the web.
Preparation:

The best way to prepare for coding interviews is to practice under similar circumstances by yourself or with a friend, using sample questions. A coding phone screen is an unnatural event, even if you are used to coding regularly for your job. The problems are different, the environment is different, and you are under time pressure.
Choose at least one language and know the basics solidly. It is better to know one language really well than multiple languages poorly. This includes creating classes and methods, conditional constructs, loops, built-in data structures, input / output, and interfacing with external processes / systems. Be prepared to use this language to solve any type of problem you may get.
Consider practicing by trying similar coding exercises here: https://www.interviewbit.com/
Facebook Engineering:

https://code.facebook.com/
https://www.facebook.com/Engineering
Additional Coding Prep Resources:

https://vimeo.com/275298962 Password: 2018prep

https://interviewing.io/ This site is a technical interview program that allows candidates to practice coding interviews, technical interviews, etc. with engineers from companies like Facebook, Google and Amazon, that provides live feedback on every interview. Our candidates have found this useful hence sharing it here!

Cracking the Facebook Coding Interview - The Approach:

https://vimeo.com/interviewprepsession/theapproach Password: FB_IPS

Cracking the Facebook Coding Interview- Problem Walk-Through:

https://vimeo.com/interviewprepsession/problemwalkthrough Password: FB_IPS

 

Coding Sample question:

# Facebook logo stickers cost $2 each from the company store. I have an idea
# I want to cut up the stickers, and use the letters to make other words/phrases.
# A Facebook logo sticker contains only the word 'facebook', in all lower-case letters.
#
# Write a function that, given a string consisting of a word or words made up
# of letters from the word 'facebook', outputs an integer with the number of
# stickers I will need to buy.
#
# get_num_stickers('coffee kebab') -> 3
# get_num_stickers('book') -> 1
# get_num_stickers('ffacebook') -> 2
#
# You can assume the input you are passed is valid, that is, does not contain
# any non-'facebook' letters, and the only potential non-letter characters
# in the string are spaces.

 

Again, the first interview you will have will only cover your coding ability, but here are other resources to review your systems knowledge for the later stages of the interview process, as we discussed:

 

SYSTEMS

 

Types of Questions Asked:

The Systems interviews generally covers at least one the following topics:

Linux Internals
Troubleshooting
Linux Internals:

The Systems interview is designed to evaluate your knowledge of Linux internals and topics can include, but are not limited to:

Process Execution and/or Threads
Memory Usage
RAID Levels
The kernel and how it interacts with other system components
System Calls
Signals and Signal Handlers
Modern Web Architectures and Webservers
Tips:

No one tool or topic is critical, but a broad familiarity with each of these spaces and the ability to apply that knowledge to new situations is important. Everything from the kernel to the user space is fair game, and we look for both breadth and depth of knowledge.

 

Preparation:

Review Linux system fundamentals and the topics mentioned above.

Review userspace/Kernel space boundaries and interactions.

Examples might include: ioctls, sysctls, context switches.

Troubleshooting:

The Engineer will lay out a system related issue or problem that you are seeing in the infrastructure and ask you to troubleshoot it. As you take each step, the Engineer will provide the hypothetical system output to prompt you to the next step.

Here is an example exchange:

Interviewer: 'You're seeing this in the infrastructure. How would you troubleshoot it?'

Interviewee: 'I'd check this first'

Interviewer: 'OK, you get this in response. What next?'

Interviewee: 'I'd run this command next'

A second scenario might involve having you analyze Linux/Unix system performance using various tools. The expectation would be for you to identify what the potential issues might be and your approach for resolving them.

 

Tips:

We’re looking for a structured, methodical approach. Narrow down potential issues systematically as you zero in on the root cause.
Be open about what you know and don’t know. One of the goals is to find the limits of your knowledge and see how you react outside of that so always attempt to answer the question at hand. The interviewer will provide hints along the way if you get stuck.
Ask clarifying questions whenever necessary.
Think through your solutions out loud, and share as much relevant knowledge as possible.
Again, please make sure you are in a quiet place with a reliable internet connection.
Preparation: 

Review troubleshooting tools for system-level performance issues.