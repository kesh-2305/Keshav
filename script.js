const questions = [
  {
    category: "History",
    question: "Which city is the capital of Haryana?",
    options: ["Delhi", "Chandigarh", "Jaipur", "Lucknow"],
    answer: "Chandigarh",
    explanation: "Chandigarh serves as the joint capital of Punjab and Haryana."
  },
  {
    category: "Geography",
    question: "Which river is closely associated with Haryana?",
    options: ["Ganga", "Yamuna", "Brahmaputra", "Godavari"],
    answer: "Yamuna",
    explanation: "The Yamuna river is closely connected with Haryana's geography."
  },
  {
    category: "Politics",
    question: "Who is the current Chief Minister of Haryana?",
    options: ["Manohar Lal Khattar", "Bhupinder Singh Hooda", "Nayab Singh Saini", "Kiran Choudhry"],
    answer: "Nayab Singh Saini",
    explanation: "Nayab Singh Saini is the current Chief Minister of Haryana."
  },
  {
    category: "Current Affairs",
    question: "Which Haryana city is famous for the IT and business hub?",
    options: ["Gurugram", "Hisar", "Rohtak", "Karnal"],
    answer: "Gurugram",
    explanation: "Gurugram is a major IT and business hub in Haryana."
  },
  {
    category: "Culture",
    question: "What is the state animal of Haryana?",
    options: ["Tiger", "Nilgai", "Elephant", "Lion"],
    answer: "Nilgai",
    explanation: "The Nilgai is the state animal of Haryana."
  },
  {
    category: "Culture",
    question: "What is the state bird of Haryana?",
    options: ["Peacock", "Sparrow", "Eagle", "Duck"],
    answer: "Peacock",
    explanation: "The Peacock is the state bird of Haryana."
  },
  {
    category: "Geography",
    question: "Which national park is located in Haryana?",
    options: ["Kaziranga", "Ranthambore", "Sultanpur National Park", "Jim Corbett"],
    answer: "Sultanpur National Park",
    explanation: "Sultanpur National Park is a major wetland and bird sanctuary in Haryana."
  },
  {
    category: "History",
    question: "Which crop is Haryana especially known for?",
    options: ["Tea", "Basmati rice", "Coffee", "Sugarcane"],
    answer: "Basmati rice",
    explanation: "Haryana is well known for Basmati rice production."
  }
];

const categories = ["All", "History", "Geography", "Politics", "Current Affairs", "Culture"];

let selectedCategory = "All";
let selectedMode = "quiz";
let currentQuestions = [];
let currentIndex = 0;
let score = 0;
let correctCount = 0;
let wrongCount = 0;
let currentSelection = null;
let answered = false;
let bookmarks = JSON.parse(localStorage.getItem("haryanaBookmarks") || "[]");
let leaderboard = JSON.parse(localStorage.getItem("haryanaLeaderboard") || "[]");

const categoryButtonsContainer = document.getElementById("categoryButtons");
const questionCard = document.getElementById("questionCard");
const resultCard = document.getElementById("resultCard");
const questionText = document.getElementById("questionText");
const optionsContainer = document.getElementById("optionsContainer");
const feedback = document.getElementById("feedback");
const scoreValue = document.getElementById("scoreValue");
const progressValue = document.getElementById("progressValue");
const correctValue = document.getElementById("correctValue");
const wrongValue = document.getElementById("wrongValue");
const resultText = document.getElementById("resultText");
const accuracyText = document.getElementById("accuracyText");
const bookmarkList = document.getElementById("bookmarkList");
const leaderboardList = document.getElementById("leaderboardList");

function renderCategoryButtons() {
  categoryButtonsContainer.innerHTML = "";
  categories.forEach((cat) => {
    const btn = document.createElement("button");
    btn.textContent = cat;
    btn.className = selectedCategory === cat ? "active" : "";
    btn.addEventListener("click", () => {
      selectedCategory = cat;
      renderCategoryButtons();
    });
    categoryButtonsContainer.appendChild(btn);
  });
}

function getFilteredQuestions() {
  if (selectedCategory === "All") return questions;
  return questions.filter((q) => q.category === selectedCategory);
}

function updateStats() {
  scoreValue.textContent = score;
  progressValue.textContent = `${Math.min(currentIndex + (answered ? 1 : 0), currentQuestions.length)}/${currentQuestions.length}`;
  correctValue.textContent = correctCount;
  wrongValue.textContent = wrongCount;
}

function renderQuestion() {
  if (!currentQuestions.length) return;
  const q = currentQuestions[currentIndex];
  questionCard.classList.remove("hidden");
  resultCard.classList.add("hidden");
  questionText.textContent = `${currentIndex + 1}. ${q.question}`;
  optionsContainer.innerHTML = "";
  feedback.textContent = "";
  currentSelection = null;
  answered = false;

  q.options.forEach((option) => {
    const btn = document.createElement("button");
    btn.className = "option";
    btn.textContent = option;
    btn.addEventListener("click", () => selectOption(option));
    optionsContainer.appendChild(btn);
  });

  updateStats();
}

function selectOption(option) {
  if (answered) return;
  const currentQuestion = currentQuestions[currentIndex];
  currentSelection = option;
  answered = true;
  const buttons = optionsContainer.querySelectorAll("button");

  buttons.forEach((btn) => {
    btn.classList.remove("selected");
    if (btn.textContent === option) {
      btn.classList.add("selected");
    }
    if (btn.textContent === currentQuestion.answer) {
      btn.classList.add("correct");
    } else if (btn.textContent === option && option !== currentQuestion.answer) {
      btn.classList.add("wrong");
    }
  });

  if (option === currentQuestion.answer) {
    score += 10;
    correctCount += 1;
    feedback.textContent = `Correct! ${currentQuestion.explanation}`;
  } else {
    wrongCount += 1;
    feedback.textContent = `Wrong. ${currentQuestion.explanation}`;
  }

  updateStats();
}

function showResult() {
  questionCard.classList.add("hidden");
  resultCard.classList.remove("hidden");
  const total = currentQuestions.length;
  const accuracy = total ? Math.round((correctCount / total) * 100) : 0;
  resultText.textContent = `You scored ${score} points with ${correctCount} correct answers out of ${total}.`;
  accuracyText.textContent = `Accuracy: ${accuracy}%`;

  leaderboard.push({ score, correctCount, total, accuracy });
  leaderboard.sort((a, b) => b.score - a.score);
  leaderboard = leaderboard.slice(0, 5);
  localStorage.setItem("haryanaLeaderboard", JSON.stringify(leaderboard));
  renderLeaderboard();
}

function nextQuestion() {
  if (currentIndex < currentQuestions.length - 1) {
    currentIndex += 1;
    renderQuestion();
  } else {
    showResult();
  }
}

function startQuiz(useDailyQuiz = false) {
  currentQuestions = getFilteredQuestions();
  if (useDailyQuiz) {
    currentQuestions = [...currentQuestions].sort(() => 0.5 - Math.random()).slice(0, 5);
  }
  currentIndex = 0;
  score = 0;
  correctCount = 0;
  wrongCount = 0;
  answered = false;
  currentSelection = null;
  renderQuestion();
}

function renderBookmarks() {
  bookmarkList.innerHTML = "";
  if (!bookmarks.length) {
    bookmarkList.innerHTML = "<li>No bookmarked questions yet.</li>";
    return;
  }
  bookmarks.forEach((item) => {
    const li = document.createElement("li");
    li.textContent = item;
    bookmarkList.appendChild(li);
  });
}

function renderLeaderboard() {
  leaderboardList.innerHTML = "";
  if (!leaderboard.length) {
    leaderboardList.innerHTML = "<li>No scores yet.</li>";
    return;
  }
  leaderboard.forEach((entry, index) => {
    const li = document.createElement("li");
    li.textContent = `${index + 1}. Score ${entry.score} | Accuracy ${entry.accuracy}%`;
    leaderboardList.appendChild(li);
  });
}

function toggleBookmark() {
  if (!currentQuestions.length) return;
  const currentQuestion = currentQuestions[currentIndex];
  const text = `${currentQuestion.category}: ${currentQuestion.question}`;
  if (bookmarks.includes(text)) {
    bookmarks = bookmarks.filter((item) => item !== text);
    feedback.textContent = "Bookmark removed.";
  } else {
    bookmarks.push(text);
    feedback.textContent = "Bookmark added.";
    localStorage.setItem("haryanaBookmarks", JSON.stringify(bookmarks));
  }
  localStorage.setItem("haryanaBookmarks", JSON.stringify(bookmarks));
  renderBookmarks();
}

function attachEvents() {
  document.getElementById("startBtn").addEventListener("click", () => startQuiz());
  document.getElementById("restartBtn").addEventListener("click", () => startQuiz());
  document.getElementById("submitBtn").addEventListener("click", () => {
    if (!answered) {
      feedback.textContent = "Please select an option first.";
      return;
    }
    if (selectedMode === "quiz") {
      document.getElementById("nextBtn").classList.remove("hidden");
    } else {
      nextQuestion();
    }
  });
  document.getElementById("nextBtn").addEventListener("click", nextQuestion);
  document.getElementById("bookmarkBtn").addEventListener("click", toggleBookmark);
  document.getElementById("dailyQuizBtn").addEventListener("click", () => startQuiz(true));
  document.querySelectorAll(".mode-btn").forEach((btn) => {
    btn.addEventListener("click", () => {
      selectedMode = btn.getAttribute("data-mode");
      document.querySelectorAll(".mode-btn").forEach((b) => b.classList.toggle("active", b === btn));
    });
  });
}

renderCategoryButtons();
attachEvents();
renderBookmarks();
renderLeaderboard();
