// App.jsx - Practical 7: Counter App in React
// Demonstrates:
// 1. Components (Modular child components)
// 2. Text Interpolation ({count}, {step})
// 3. Conditional Rendering (Positive/Negative/Warning conditions)
// 4. List Rendering (History log using .map)
// 5. Form Handling (Form to configure step & log custom notes)

// Subcomponent 1: Displays the Counter value & condition
function CounterDisplay({ count }) {
    return (
        <div>
            <h2>Current Count: {count}</h2>
            {/* Conditional Rendering */}
            {count > 0 && <p>Condition: <b>Count is Positive (+)</b></p>}
            {count < 0 && <p style={{ color: 'red' }}>Condition: <b>Count is Negative (-)</b></p>}
            {count === 0 && <p>Condition: <b>Count is Neutral (Zero)</b></p>}
            {Math.abs(count) >= 20 && <p style={{ color: 'orange' }}><b>Warning: Threshold of 20 exceeded!</b></p>}
        </div>
    );
}

// Subcomponent 2: Action Buttons
function CounterControls({ onIncrement, onDecrement, onReset, step }) {
    return (
        <div>
            <button onClick={onDecrement}>Decrement (-{step})</button>{' '}
            <button onClick={onReset}>Reset</button>{' '}
            <button onClick={onIncrement}>Increment (+{step})</button>
        </div>
    );
}

// Subcomponent 3: Form Handling
function ConfigForm({ step, onStepChange, onAddNote }) {
    const [noteText, setNoteText] = React.useState('');

    const handleFormSubmit = (e) => {
        e.preventDefault();
        if (noteText.trim()) {
            onAddNote(noteText);
            setNoteText('');
        }
    };

    return (
        <form onSubmit={handleFormSubmit}>
            <h3>Form Handling (Configure Settings)</h3>
            <table>
                <tbody>
                    <tr>
                        <td>Change Step Value:</td>
                        <td>
                            <input
                                type="number"
                                value={step}
                                onChange={(e) => onStepChange(Number(e.target.value) || 1)}
                                min="1"
                            />
                        </td>
                    </tr>
                    <tr>
                        <td>Add Note / Log:</td>
                        <td>
                            <input
                                type="text"
                                value={noteText}
                                onChange={(e) => setNoteText(e.target.value)}
                                placeholder="e.g. Test increment"
                            />
                            {' '}
                            <button type="submit">Submit Note</button>
                        </td>
                    </tr>
                </tbody>
            </table>
        </form>
    );
}

// Subcomponent 4: List Rendering
function HistoryList({ history }) {
    return (
        <div>
            <h3>Counter History Log (List Rendering)</h3>
            {/* Conditional Rendering for empty state */}
            {history.length === 0 ? (
                <p>No activity recorded yet.</p>
            ) : (
                <table border="1" cellPadding="5">
                    <thead>
                        <tr>
                            <th>#</th>
                            <th>Action</th>
                            <th>Count Value</th>
                            <th>Note / Details</th>
                            <th>Timestamp</th>
                        </tr>
                    </thead>
                    <tbody>
                        {/* List Rendering using .map() */}
                        {history.map((item, index) => (
                            <tr key={item.id}>
                                <td>{index + 1}</td>
                                <td>{item.action}</td>
                                <td>{item.value}</td>
                                <td>{item.note}</td>
                                <td>{item.time}</td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            )}
        </div>
    );
}

// Main Component
function App() {
    const [count, setCount] = React.useState(0);
    const [step, setStep] = React.useState(1);
    const [history, setHistory] = React.useState([]);

    const logHistory = (action, val, note) => {
        const newEntry = {
            id: Date.now() + Math.random(),
            action: action,
            value: val,
            note: note || '-',
            time: new Date().toLocaleTimeString()
        };
        setHistory((prev) => [newEntry, ...prev]);
    };

    const handleIncrement = () => {
        const nextVal = count + step;
        setCount(nextVal);
        logHistory('Increment', nextVal, 'Added ' + step);
    };

    const handleDecrement = () => {
        const nextVal = count - step;
        setCount(nextVal);
        logHistory('Decrement', nextVal, 'Subtracted ' + step);
    };

    const handleReset = () => {
        setCount(0);
        logHistory('Reset', 0, 'Reset back to zero');
    };

    const handleAddNote = (note) => {
        logHistory('User Note', count, note);
    };

    return (
        <div>
            <h1>Practical 7: React Counter Application</h1>
            <p>Demonstrating Components, Conditional Rendering, List Rendering, Text Interpolation, and Form Handling</p>
            <hr />

            {/* Subcomponents */}
            <CounterDisplay count={count} />
            <br />
            <CounterControls
                onIncrement={handleIncrement}
                onDecrement={handleDecrement}
                onReset={handleReset}
                step={step}
            />
            <hr />
            <ConfigForm
                step={step}
                onStepChange={setStep}
                onAddNote={handleAddNote}
            />
            <hr />
            <HistoryList history={history} />
        </div>
    );
}
