# AI Assistant Project: OOP & Data Types Exploration

## Overview

This project is a mini simulation of a modular AI assistant (like Siri, Alexa, or ChatGPT), implemented in Python using core concepts from Object-Oriented Programming (OOP) and diverse data types. The assistant can handle personalized tasks for different users—such as music recommendations, workout suggestions, and study planning—demonstrating the use of encapsulation, inheritance, and polymorphism.

## Features

* **UserProfile**: Models a user with name, age, preferences, and premium status.
* **Request**: Models a user request with input string, timestamp, and classified command type.
* **Response**: Models an assistant’s response with message, confidence score, and action indicator.
* **OOP Design**: Base `AIAssistant` class with specialized subclasses (`MusicAssistant`, `FitnessAssistant`, `StudyAssistant`), each with unique behavior.
* **Polymorphism**: Different assistant subclasses respond appropriately to user requests.
* **Type Safety & Validation**: Each data class checks that its inputs are of the correct type and within expected values.
* **Simple Command Parsing**: Classifies user input into intent categories using basic string matching.

## File Structure

```
main.py
README.md
```

## Example Output

```
Hello, Alice! How can I help you today?
Response: Here's a Chill Vibes Playlist for you! | Confidence: 0.95 | Action: True
----------------------------------------
Hello, Bob! How can I help you today?
Response: Suggested workout: Strength Workout Routine. | Confidence: 0.9 | Action: True
----------------------------------------
Hello, Carol! How can I help you today?
Response: Scheduled a study session for history. | Confidence: 0.92 | Action: True
----------------------------------------
```

