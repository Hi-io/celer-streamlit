# CelerAI

CelerConnect is a platform that uses artificial intelligence to automate and accelerate communication between companies and their customers. It's capable of receiving messages through different media such as Discord, WhatsApp, email, etc. and categorizing them to determine which department they belong to. If it's a common problem with a replicable solution, our AI will automatically respond. If not, the AI will send a message to the customer informing them that their request has been received and will be attended to soon. Meanwhile, the AI will summarize and send it to the corresponding department.

## Table of Contents

- Problem
- Solution
- Functioning
- Functionalities
- Conclutions

Have you ever been frustrated by the slowness and hassle of communication with companies? Have you ever felt lost in a maze of channels and filters? Well, our company has the solution! We've created a platform that uses artificial intelligence to automate and accelerate communication between companies and their customers.

## Problem

The problem that many companies face is that communications with customers are often slow and cumbersome. Imagine needing help and having to go through different channels and filters to reach someone who can assist you. This can be frustrating and can take a lot of time. Additionally, hiring someone to exclusively handle this work can be very expensive, which means that many companies simply don't have the resources to do it.

## Solution

Our solution is a complete platform that uses artificial intelligence. It's capable of receiving messages through different media such as Discord, WhatsApp, email, etc. and categorizing them to determine which department they belong to. If it's a common problem with a replicable solution, our AI will automatically respond. If not, the AI will send a message to the customer informing them that their request has been received and will be attended to soon. Meanwhile, the AI will summarize and send it to the corresponding department.

## Functioning

Our platform is multi-platform and extremely modular. It has three parts that work synchronously. First, we have independent receivers running on each communication medium. Second, we have the API, which receives the data, performs ETL processing, and applies different AI technologies. And finally, we have the platform to answer messages, which connects to everything else only through the API.

## Functionalities
Our project consists of the following tools, each with its unique set of functionalities:

### Unanswered Message Processing API

The Unanswered Message Processing API extracts data from a database of message requests and uses Tech-davinci003 technology to process unanswered messages. It extracts detailed information from the message, summarizes the message, and identifies the department to which the message belongs. This information can then be used to prioritize and route the message to the appropriate department. The API also automatically detects unanswered messages to execute these actions.

### Email Viewer

Email Viewer is a tool that monitors an email inbox for general queries. Upon receiving an email, it sends the message details to an API in JSON format including the date, subject, content, and platform (email). The API evaluates the email and, if approved, returns a 202 status code and loads the data. If not approved, it marks the corresponding error.

### Miku

Miku is a Discord bot that utilizes OpenAI's API, specifically the Tech Davinci 003 model. This bot is designed to help efficiently and personalizedly resolve user queries in the Discord chat. Its functionalities include message summarization, departmental classification, and problem-solving.

### Eloylit

Eloylit is a platform for centralizing user messages and queries so that a representative from the corresponding department can efficiently respond to them. Its functionalities include question and answer history, automated responses, and an intuitive user interface.

## Conclutions
In conclusion, CelerConnect offers a comprehensive solution to the problem of slow and cumbersome communication between companies and their customers. By using artificial intelligence to automate and accelerate the process, our platform enables companies to provide faster and more efficient support to their customers while reducing the cost of hiring dedicated staff. With its modular and multi-platform design, CelerConnect offers a range of tools and functionalities that can be customized to meet the specific needs of any business. Overall, CelerConnect represents a significant advancement in the field of customer communication and support.
