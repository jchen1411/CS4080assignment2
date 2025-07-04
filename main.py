from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, Optional
from enum import Enum, auto

class CommandType(Enum):
    MUSIC = auto()
    FITNESS = auto()
    STUDY = auto()
    UNKNOWN = auto()

@dataclass
class UserProfile:
    name: str
    age: int
    preferences: Dict[str, str]
    isPremium: bool

    def __post_init__(self):
        assert isinstance(self.name, str) and self.name
        assert isinstance(self.age, int) and self.age > 0
        assert isinstance(self.preferences, dict)
        assert isinstance(self.isPremium, bool)

@dataclass
class Request:
    input_str: str
    timestamp: datetime
    command_type: CommandType

    def __post_init__(self):
        assert isinstance(self.input_str, str)
        assert isinstance(self.timestamp, datetime)
        assert isinstance(self.command_type, CommandType)

@dataclass
class Response:
    message: str
    confidence: float
    actionPerformed: bool

    def __post_init__(self):
        assert isinstance(self.message, str)
        assert 0.0 <= self.confidence <= 1.0
        assert isinstance(self.actionPerformed, bool)





class AIAssistant:
    def __init__(self, user: UserProfile):
        self.user = user

    def greetUser(self) -> str:
        return f"Hello, {self.user.name}! How can I help you today?"

    def handleRequest(self, request: Request) -> Response:
        # Base: just echoes back
        return self.generateResponse("Sorry, I can't handle that request.", 0.5, False)

    def generateResponse(self, message: str, confidence: float, actionPerformed: bool) -> Response:
        return Response(message=message, confidence=confidence, actionPerformed=actionPerformed)

class MusicAssistant(AIAssistant):
    def handleRequest(self, request: Request) -> Response:
        if request.command_type == CommandType.MUSIC:
            return self.recommendPlaylist(request)
        return super().handleRequest(request)

    def recommendPlaylist(self, request: Request) -> Response:
        mood = self.user.preferences.get('mood', 'happy')
        playlist = f"{mood.title()} Vibes Playlist"
        message = f"Here's a {playlist} for you!"
        return self.generateResponse(message, 0.95, True)

class FitnessAssistant(AIAssistant):
    def handleRequest(self, request: Request) -> Response:
        if request.command_type == CommandType.FITNESS:
            return self.suggestWorkout(request)
        return super().handleRequest(request)

    def suggestWorkout(self, request: Request) -> Response:
        goal = self.user.preferences.get('fitness_goal', 'general fitness')
        workout = f"{goal.title()} Workout Routine"
        message = f"Suggested workout: {workout}."
        return self.generateResponse(message, 0.9, True)

class StudyAssistant(AIAssistant):
    def handleRequest(self, request: Request) -> Response:
        if request.command_type == CommandType.STUDY:
            return self.scheduleStudySession(request)
        return super().handleRequest(request)

    def scheduleStudySession(self, request: Request) -> Response:
        topic = self.user.preferences.get('study_topic', 'math')
        message = f"Scheduled a study session for {topic}."
        return self.generateResponse(message, 0.92, True)



import random

def command_parser(user_input: str) -> CommandType:
    user_input = user_input.lower()
    if "music" in user_input or "song" in user_input or "playlist" in user_input:
        return CommandType.MUSIC
    elif "workout" in user_input or "exercise" in user_input:
        return CommandType.FITNESS
    elif "study" in user_input or "homework" in user_input:
        return CommandType.STUDY
    else:
        return CommandType.UNKNOWN

def main():
    # Simulate user profiles
    users = [
        UserProfile(name="Alice", age=25, preferences={"mood": "chill"}, isPremium=True),
        UserProfile(name="Bob", age=30, preferences={"fitness_goal": "strength"}, isPremium=False),
        UserProfile(name="Carol", age=20, preferences={"study_topic": "history"}, isPremium=True)
    ]

    # Map assistant per user type (in a real app, could be dynamic)
    assistants = [
        MusicAssistant(users[0]),
        FitnessAssistant(users[1]),
        StudyAssistant(users[2])
    ]

    # Simulate requests
    requests = [
        Request("Play me some music", datetime.now(), command_parser("Play me some music")),
        Request("Suggest a workout", datetime.now(), command_parser("Suggest a workout")),
        Request("Schedule a study session", datetime.now(), command_parser("Schedule a study session")),
        Request("Tell me a joke", datetime.now(), command_parser("Tell me a joke"))
    ]

    for i, assistant in enumerate(assistants):
        print(assistant.greetUser())
        resp = assistant.handleRequest(requests[i])
        print(f"Response: {resp.message} | Confidence: {resp.confidence} | Action: {resp.actionPerformed}")
        print("-" * 40)

if __name__ == "__main__":
    main()
