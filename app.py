<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Knights and Knaves Interactive Puzzle Game</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            color: #333;
            line-height: 1.6;
        }

        .container {
            max-width: 900px;
            margin: 0 auto;
            padding: 20px;
        }

        .header {
            text-align: center;
            margin-bottom: 30px;
            color: white;
        }

        .header h1 {
            font-size: 2.5rem;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }

        .header p {
            font-size: 1.1rem;
            opacity: 0.9;
        }

        .progress-bar {
            background: rgba(255,255,255,0.2);
            border-radius: 10px;
            padding: 5px;
            margin-bottom: 30px;
        }

        .progress-fill {
            background: linear-gradient(45deg, #28a745, #20c997);
            height: 10px;
            border-radius: 5px;
            transition: width 0.3s ease;
            width: 0%;
        }

        .puzzle-container {
            background: white;
            border-radius: 20px;
            padding: 30px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.2);
            margin-bottom: 20px;
            min-height: 500px;
        }

        .puzzle-header {
            display: flex;
            align-items: center;
            gap: 15px;
            margin-bottom: 25px;
            padding-bottom: 15px;
            border-bottom: 3px solid #f0f0f0;
        }

        .puzzle-icon {
            font-size: 2.5rem;
        }

        .puzzle-title {
            flex: 1;
        }

        .puzzle-title h2 {
            color: #667eea;
            font-size: 1.8rem;
            margin-bottom: 5px;
        }

        .puzzle-subtitle {
            color: #666;
            font-size: 1rem;
        }

        .scenario {
            background: linear-gradient(45deg, #f8f9ff, #fff5f8);
            padding: 20px;
            border-radius: 15px;
            margin-bottom: 25px;
            border-left: 5px solid #667eea;
        }

        .character-statement {
            margin: 12px 0;
            padding: 15px;
            background: white;
            border-radius: 10px;
            border: 2px solid #e8ecff;
            box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        }

        .character-name {
            font-weight: bold;
            color: #764ba2;
            font-size: 1.1rem;
        }

        .statement-text {
            margin-top: 5px;
            font-style: italic;
            color: #444;
        }

        .question {
            font-size: 1.3rem;
            font-weight: bold;
            color: #667eea;
            margin-bottom: 20px;
            text-align: center;
        }

        .choices-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
            margin-bottom: 25px;
        }

        .choice-btn {
            padding: 15px 20px;
            border: 3px solid #e0e6ff;
            background: white;
            border-radius: 12px;
            cursor: pointer;
            transition: all 0.3s ease;
            text-align: center;
            font-size: 1.1rem;
            font-weight: 600;
            position: relative;
            overflow: hidden;
        }

        .choice-btn:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 20px rgba(0,0,0,0.15);
            border-color: #667eea;
        }

        .choice-btn.selected {
            background: linear-gradient(45deg, #667eea, #764ba2);
            color: white;
            border-color: #667eea;
        }

        .choice-btn.correct {
            background: linear-gradient(45deg, #28a745, #20c997);
            color: white;
            border-color: #28a745;
            animation: pulse 0.5s;
        }

        .choice-btn.incorrect {
            background: linear-gradient(45deg, #dc3545, #fd7e14);
            color: white;
            border-color: #dc3545;
            animation: shake 0.5s;
        }

        .choice-btn.disabled {
            opacity: 0.6;
            cursor: not-allowed;
            transform: none !important;
        }

        .choice-icon {
            font-size: 1.5rem;
            margin-right: 10px;
        }

        .knight-choice { border-left: 5px solid #28a745; }
        .knave-choice { border-left: 5px solid #dc3545; }

        .submit-btn {
            display: block;
            width: 200px;
            margin: 0 auto;
            padding: 15px 25px;
            background: linear-gradient(45deg, #667eea, #764ba2);
            color: white;
            border: none;
            border-radius: 10px;
            font-size: 1.2rem;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.3s ease;
            opacity: 0.5;
            pointer-events: none;
        }

        .submit-btn.active {
            opacity: 1;
            pointer-events: auto;
        }

        .submit-btn:hover.active {
            transform: translateY(-3px);
            box-shadow: 0 8px 20px rgba(0,0,0,0.3);
        }

        .result {
            margin-top: 25px;
            padding: 20px;
            border-radius: 15px;
            text-align: center;
            opacity: 0;
            transform: translateY(20px);
            transition: all 0.5s ease;
        }

        .result.show {
            opacity: 1;
            transform: translateY(0);
        }

        .result.correct {
            background: linear-gradient(45deg, #d4edda, #c3e6cb);
            border: 2px solid #28a745;
            color: #155724;
        }

        .result.incorrect {
            background: linear-gradient(45deg, #f8d7da, #f1b0b7);
            border: 2px solid #dc3545;
            color: #721c24;
        }

        .result-icon {
            font-size: 3rem;
            margin-bottom: 10px;
        }

        .result-title {
            font-size: 1.5rem;
            font-weight: bold;
            margin-bottom: 10px;
        }

        .explanation {
            margin-top: 15px;
            font-size: 1rem;
            line-height: 1.6;
            text-align: left;
        }

        .next-btn {
            margin-top: 20px;
            padding: 12px 25px;
            background: linear-gradient(45deg, #28a745, #20c997);
            color: white;
            border: none;
            border-radius: 8px;
            font-size: 1.1rem;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.3s ease;
        }

        .next-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        }

        .final-score {
            text-align: center;
            padding: 30px;
            background: linear-gradient(45deg, #fff, #f8f9ff);
            border-radius: 20px;
            margin-top: 20px;
        }

        .score-display {
            font-size: 2rem;
            font-weight: bold;
            margin-bottom: 15px;
        }

        .restart-btn {
            padding: 15px 30px;
            background: linear-gradient(45deg, #667eea, #764ba2);
            color: white;
            border: none;
            border-radius: 10px;
            font-size: 1.2rem;
            font-weight: bold;
            cursor: pointer;
            margin-top: 20px;
        }

        .hint-btn {
            position: absolute;
            top: 20px;
            right: 20px;
            background: rgba(255,255,255,0.9);
            border: 2px solid #ffc107;
            color: #856404;
            padding: 8px 15px;
            border-radius: 8px;
            cursor: pointer;
            font-size: 0.9rem;
            transition: all 0.3s ease;
        }

        .hint-btn:hover {
            background: #ffc107;
            color: white;
        }

        .hint {
            background: #fff3cd;
            border: 1px solid #ffc107;
            color: #856404;
            padding: 15px;
            border-radius: 10px;
            margin: 15px 0;
            opacity: 0;
            transform: translateY(-10px);
            transition: all 0.3s ease;
        }

        .hint.show {
            opacity: 1;
            transform: translateY(0);
        }

        @keyframes pulse {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.05); }
        }

        @keyframes shake {
            0%, 100% { transform: translateX(0); }
            25% { transform: translateX(-5px); }
            75% { transform: translateX(5px); }
        }

        @media (max-width: 768px) {
            .container { padding: 15px; }
            .header h1 { font-size: 2rem; }
            .choices-grid { grid-template-columns: 1fr; }
            .puzzle-container { padding: 20px; }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🎮 Knights & Knaves Interactive Puzzle</h1>
            <p>Can you solve these logic puzzles? Choose who is a Knight and who is a Knave!</p>
        </div>

        <div class="progress-bar">
            <div class="progress-fill" id="progressBar"></div>
        </div>

        <div class="puzzle-container">
            <button class="hint-btn" onclick="toggleHint()">💡 Need a Hint?</button>
            
            <div class="puzzle-header">
                <span class="puzzle-icon" id="puzzleIcon">🏰</span>
                <div class="puzzle-title">
                    <h2 id="puzzleTitle">Puzzle 1: The Paradox</h2>
                    <div class="puzzle-subtitle" id="puzzleSubtitle">Read the scenario and make your choice</div>
                </div>
            </div>

            <div class="scenario" id="scenario">
                <!-- Puzzle scenario will be inserted here -->
            </div>

            <div class="hint" id="hint">
                <!-- Hint will be inserted here -->
            </div>

            <div class="question" id="question">
                Who is a Knight and who is a Knave?
            </div>

            <div class="choices-grid" id="choicesGrid">
                <!-- Choice buttons will be inserted here -->
            </div>

            <button class="submit-btn" id="submitBtn" onclick="checkAnswer()">
                🎯 Submit Answer
            </button>

            <div class="result" id="result">
                <!-- Result will be shown here -->
            </div>
        </div>

        <div class="final-score" id="finalScore" style="display: none;">
            <h2>🎉 Puzzle Complete!</h2>
            <div class="score-display" id="scoreDisplay"></div>
            <p>Great job solving these logical puzzles!</p>
            <button class="restart-btn" onclick="restartGame()">🔄 Play Again</button>
        </div>
    </div>

    <script>
        let currentPuzzle = 0;
        let score = 0;
        let userAnswers = {};
        let showingHint = false;

        const puzzles = [
            {
                icon: "🏰",
                title: "Puzzle 1: The Paradox",
                subtitle: "A single character makes an impossible claim",
                scenario: `
                    <div class="character-statement">
                        <div class="character-name">🤴 Character A says:</div>
                        <div class="statement-text">"I am both a knight and a knave."</div>
                    </div>
                `,
                characters: ['A'],
                correctAnswers: { 'A': 'Knave' },
                hint: "Think about it: If A is a knight, then the statement must be true. But can someone be both a knight AND a knave at the same time? If A is a knave, then the statement must be false. Is 'I am both a knight and a knave' false when A is only a knave?",
                explanation: "A claims to be both a knight and a knave, which is impossible. If A were a knight, the statement would have to be true, but being both is impossible. If A is a knave, the statement is false (A is NOT both), which is consistent with knaves lying."
            },
            {
                icon: "👥", 
                title: "Puzzle 2: The Accusation",
                subtitle: "One character makes a claim about both of them",
                scenario: `
                    <div class="character-statement">
                        <div class="character-name">🤴 Character A says:</div>
                        <div class="statement-text">"We are both knaves."</div>
                    </div>
                    <div class="character-statement">
                        <div class="character-name">👑 Character B says:</div>
                        <div class="statement-text">Nothing.</div>
                    </div>
                `,
                characters: ['A', 'B'],
                correctAnswers: { 'A': 'Knave', 'B': 'Knight' },
                hint: "If A is a knight, then 'we are both knaves' must be true. But if A is a knight, how can A also be a knave? If A is a knave, then the statement must be false. What does 'we are both knaves' being false tell us about B?",
                explanation: "If A were a knight, then 'we are both knaves' would be true, making A a knave (contradiction). So A must be a knave, making the statement false. Since the statement is false, they are NOT both knaves, so B must be a knight."
            },
            {
                icon: "⚡",
                title: "Puzzle 3: The Contradiction", 
                subtitle: "Two characters make opposite claims",
                scenario: `
                    <div class="character-statement">
                        <div class="character-name">🤴 Character A says:</div>
                        <div class="statement-text">"We are the same kind."</div>
                    </div>
                    <div class="character-statement">
                        <div class="character-name">👑 Character B says:</div>
                        <div class="statement-text">"We are of different kinds."</div>
                    </div>
                `,
                characters: ['A', 'B'],
                correctAnswers: { 'A': 'Knave', 'B': 'Knight' },
                hint: "A and B are making opposite claims - they can't both be right! If A is a knight saying 'we are the same kind', then B must also be a knight. But then what would knight B be doing making a false statement? Try the other possibility.",
                explanation: "A and B make contradictory statements. If A were a knight (telling truth), then they're the same kind, so B would be a knight too. But then B (knight) would be lying about being different kinds (impossible). So A must be a knave, making them different kinds, and B's statement true."
            },
            {
                icon: "🎭",
                title: "Puzzle 4: The Web of Lies",
                subtitle: "The most complex puzzle with three characters",
                scenario: `
                    <div class="character-statement">
                        <div class="character-name">🤴 Character A says:</div>
                        <div class="statement-text">Either "I am a knight" OR "I am a knave" (but you don't know which).</div>
                    </div>
                    <div class="character-statement">
                        <div class="character-name">👑 Character B says:</div>
                        <div class="statement-text">"A said 'I am a knave'."</div>
                    </div>
                    <div class="character-statement">
                        <div class="character-name">🏃 Character B also says:</div>
                        <div class="statement-text">"C is a knave."</div>
                    </div>
                    <div class="character-statement">
                        <div class="character-name">👸 Character C says:</div>
                        <div class="statement-text">"A is a knight."</div>
                    </div>
                `,
                characters: ['A', 'B', 'C'],
                correctAnswers: { 'A': 'Knight', 'B': 'Knave', 'C': 'Knight' },
                hint: "Here's the key insight: Can anyone EVER say 'I am a knave'? Think about it - if a knight said it, it would be false (but knights tell truth). If a knave said it, it would be true (but knaves lie). So what does this tell us about B's claim?",
                explanation: "The key insight: Nobody can ever say 'I am a knave' because it creates a paradox. So B's claim that A said this must be false, making B a knave. Since B is a knave, 'C is a knave' is false, so C is a knight. C (knight) says 'A is a knight', which must be true."
            }
        ];

        function loadPuzzle() {
            const puzzle = puzzles[currentPuzzle];
            
            document.getElementById('puzzleIcon').textContent = puzzle.icon;
            document.getElementById('puzzleTitle').textContent = puzzle.title;
            document.getElementById('puzzleSubtitle').textContent = puzzle.subtitle;
            document.getElementById('scenario').innerHTML = puzzle.scenario;
            document.getElementById('hint').textContent = puzzle.hint;
            
            // Update progress
            const progress = ((currentPuzzle + 1) / puzzles.length) * 100;
            document.getElementById('progressBar').style.width = progress + '%';
            
            // Generate choices
            generateChoices(puzzle.characters);
            
            // Reset UI
            document.getElementById('result').classList.remove('show');
            document.getElementById('submitBtn').classList.remove('active');
            document.getElementById('hint').classList.remove('show');
            showingHint = false;
            userAnswers = {};
        }

        function generateChoices(characters) {
            const grid = document.getElementById('choicesGrid');
            grid.innerHTML = '';
            
            characters.forEach(char => {
                // Knight choice
                const knightBtn = document.createElement('div');
                knightBtn.className = 'choice-btn knight-choice';
                knightBtn.innerHTML = `<span class="choice-icon">⚔️</span>${char} is a Knight`;
                knightBtn.onclick = () => selectChoice(char, 'Knight', knightBtn);
                grid.appendChild(knightBtn);
                
                // Knave choice  
                const knaveBtn = document.createElement('div');
                knaveBtn.className = 'choice-btn knave-choice';
                knaveBtn.innerHTML = `<span class="choice-icon">🃏</span>${char} is a Knave`;
                knaveBtn.onclick = () => selectChoice(char, 'Knave', knaveBtn);
                grid.appendChild(knaveBtn);
            });
        }

        function selectChoice(character, type, button) {
            // Remove previous selection for this character
            const allBtns = document.querySelectorAll('.choice-btn');
            allBtns.forEach(btn => {
                if (btn.textContent.includes(character)) {
                    btn.classList.remove('selected');
                }
            });
            
            // Select new choice
            button.classList.add('selected');
            userAnswers[character] = type;
            
            // Check if all characters have been assigned
            const puzzle = puzzles[currentPuzzle];
            if (Object.keys(userAnswers).length === puzzle.characters.length) {
                document.getElementById('submitBtn').classList.add('active');
            }
        }

        function checkAnswer() {
            const puzzle = puzzles[currentPuzzle];
            const correct = JSON.stringify(userAnswers) === JSON.stringify(puzzle.correctAnswers);
            
            if (correct) {
                score++;
                showResult(true, puzzle.explanation);
            } else {
                showResult(false, puzzle.explanation);
            }
            
            // Disable all choice buttons
            const allBtns = document.querySelectorAll('.choice-btn');
            allBtns.forEach(btn => {
                btn.classList.add('disabled');
                
                // Show correct/incorrect styling
                const character = btn.textContent.match(/([A-C])/)[1];
                const type = btn.textContent.includes('Knight') ? 'Knight' : 'Knave';
                
                if (puzzle.correctAnswers[character] === type) {
                    btn.classList.add('correct');
                } else if (userAnswers[character] === type) {
                    btn.classList.add('incorrect');
                }
            });
            
            document.getElementById('submitBtn').style.display = 'none';
        }

        function showResult(isCorrect, explanation) {
            const resultDiv = document.getElementById('result');
            
            if (isCorrect) {
                resultDiv.className = 'result correct show';
                resultDiv.innerHTML = `
                    <div class="result-icon">🎉</div>
                    <div class="result-title">Correct! Well done!</div>
                    <div class="explanation"><strong>Explanation:</strong> ${explanation}</div>
                    ${currentPuzzle < puzzles.length - 1 ? '<button class="next-btn" onclick="nextPuzzle()">Next Puzzle ➡️</button>' : '<button class="next-btn" onclick="showFinalScore()">See Final Score 🏆</button>'}
                `;
            } else {
                resultDiv.className = 'result incorrect show';
                resultDiv.innerHTML = `
                    <div class="result-icon">❌</div>
                    <div class="result-title">Not quite right! Try again?</div>
                    <div class="explanation"><strong>Here's why:</strong> ${explanation}</div>
                    ${currentPuzzle < puzzles.length - 1 ? '<button class="next-btn" onclick="nextPuzzle()">Next Puzzle ➡️</button>' : '<button class="next-btn" onclick="showFinalScore()">See Final Score 📊</button>'}
                `;
            }
        }

        function nextPuzzle() {
            currentPuzzle++;
            if (currentPuzzle < puzzles.length) {
                loadPuzzle();
            } else {
                showFinalScore();
            }
        }

        function showFinalScore() {
            document.querySelector('.puzzle-container').style.display = 'none';
            const finalScoreDiv = document.getElementById('finalScore');
            finalScoreDiv.style.display = 'block';
            
            const percentage = Math.round((score / puzzles.length) * 100);
            let message = '';
            
            if (percentage === 100) {
                message = '🏆 Perfect Score! You\'re a logic master!';
            } else if (percentage >= 75) {
                message = '🌟 Excellent work! You have great logical reasoning skills!';
            } else if (percentage >= 50) {
                message = '👍 Good job! You\'re getting the hang of it!';
            } else {
                message = '📚 Keep practicing! Logic puzzles take time to master!';
            }
            
            document.getElementById('scoreDisplay').innerHTML = `
                ${score}/${puzzles.length} (${percentage}%)
                <br><small>${message}</small>
            `;
        }

        function restartGame() {
            currentPuzzle = 0;
            score = 0;
            document.querySelector('.puzzle-container').style.display = 'block';
            document.getElementById('finalScore').style.display = 'none';
            loadPuzzle();
        }

        function toggleHint() {
            const hint = document.getElementById('hint');
            showingHint = !showingHint;
            hint.classList.toggle('show', showingHint);
        }

        // Initialize the game
        loadPuzzle();
    </script>
</body>
</html>
