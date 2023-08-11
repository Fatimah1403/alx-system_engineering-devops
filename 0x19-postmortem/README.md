# SERVER OUTAGE POSTMETUM
> By Fatimah Hassan

![](https://www.canva.com/design/DAFrPslHNH8/GwAJbO5b6A3q0HJCGkuWzQ/edit)

## <strong>Postmortem: Web Stack Outage incident</strong>

## <strong>Issue Summary: </strong>

Duration: July 24, 2023,  03:45 PM - 10:30 PM (UTC)
Impact: A crucial outage in my two web servers and my load balancer resulted in me missing man
deadlines and unable to deploy files to the server


## <strong>Root Cause: </strong>
The root cause was initially due to a network problem. It was later cleared that the installation of MySQL caused it;
the repository of MYSQL was seen twice in the sources.list of the file, thereby causing repetition and breakdown

## <strong>Timeline: </strong>
| Time (UTC) | Actions |
|  --------- | ------- |
| 03:45 PM   | Isue detection        |
| 03:50	PM   | Assistance from a collegue |
| 04:15 PM   | Network problem detected |
| 05:00 PM   | Suspecting the issue |
| 07:00 PM   | More complex arise |
| 10:00 PM   | Root cause detected |
| 10:30 PM   | Issue resolved |

### Details
- 03:45 PM: The issue was detected when I tried to install MYSQL, and the terminal showed  Failed
to fetch http://security.ubuntu.com/ubuntu/dists/focal-security/InRelease  Temporary failure resolving 'security.ubuntu.com'.
- 03:50 PM: A colleague of mine was alerted to let us work together to solve it.
- 04:15 PM: The network problem was detected.
- 5:00 PM After solving the network issue, we went on a break to brainstorm.
- 7:00 PM: Despite scaling, the issue persisted; suspicions of a more complex problem arose
- 10:00 PM: The root cause was the repetition of two repositories inside the sources.list file was detected.
- 10:30 PM: the issue was solved, removing one repository link, and the servers returned to work.

## <strong>Root Cause and Resolution: </strong>
Root Cause: All the servers running down was caused by installing the MYSQL repository; two links of the same repository were added.

Resolution:  The link responsible for the outage was removed, and proper connection management was implemented to ensure connections were correctly made.

## <strong>Corrective and Preventative Measures: </strong>
Improvements/Fixes:
Proper documentation on Ubuntu on Microsoft site was checked
Share the knowledge among peers.


Tasks to Address the Issue:
1. Conduct a thorough check of each files in the etc directory of the server to identify and rectify any other instance related to server runtime shortage
2. Collaborate with peers and colleagues to quickly find solutions to avoid escalating things.

## <strong>Conclusion: </strong>
The server's runtime outage resulted from unforeseen circumstances caused by performance degradation and intermittent errors for a significant portion of our user base. Swift and collaborative investigation, along with proper code fixes, led to the timely resolution of the issue.




















