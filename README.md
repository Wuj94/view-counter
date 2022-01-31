# Python Test

In this project I've implemented a simple cloud-native application using Python, AWS Lambda and AWS API Gateway.

# Background

In a network of HTTP servers spread in multiple data centers, HTTP requests from
our clients’ websites are received in real time. Each of these requests contain a JSON payload describing the
events that were observed on the page. This server fleet processes over a billion requests, per day 
(hence the focus on performance).

# Task 

Design and implement a utility to process a stream of JSON messages and
calculate the number of unique viewers per day for each URL in the stream.

Sample message (JSON):

userid: A unique ID representing the user
url : The URL the visitor has accessed
type: The HTTP method used to access the URL
timestamp: The timestamp for when the action occurred

## Further notes

You should not spend more than two hours on this task. Ensure that the solution is efficient and
well tested. The choice of language and toolkit is up to you. The ideal solution should not have any
external dependencies.

## Solution

The solution follows this flow diagram.

![FlowDiagram](https://github.com/Wuj94/hitcounter/blob/b83572311ef3642945e6274cdf3162a5774c299a/Cloud%20Diagram%20-%20View%20Counter.png)
