import React, { useState } from 'react';

// Subcomponent 1: Display
function CounterDisplay({ count }) {
    return (
        <div>
            <h2>Current Count: {count}</h2>
            {count > 0 && <p>Condition: <b>Count is Positive (+)</b></p>}
            {count < 0 && <p style={{ color: 'red' }}>Condition: <b>Count is Negative (-)</b></p>}
            {count === 0 && <p>Condition: <b>Count is Zero</b></p>}
            {Math.abs(count) >= 20 && <p style={{ color: 'orange' }}><b>Warning: Threshold of 20 exceeded!</b></p>}
        </div>
    );
}

// Subcomponent 2: Controls
function CounterControls({ onIncrement, onDecrement, onReset, step }) {
    return (
        <div>
            <button onClick={onDecrement}>Decrement (-{step})</button>{' '}
            <button onClick={onReset}>Reset</button>{' '}
            <button onClick={onIncrement}>Increment (+{step})</button>
        </div>
    );
}

// Subcomponent 3: Form
function ConfigForm({ step, onStepChange, onAddNote }) {
    const [note, setNote] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        if (note.trim()) {
            onAddNote(note);
            setNote('');
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <h3>Form Handling (Step & Log)</h3>
            <table>
                <tbody>
                    <tr>
                        <td>Step Size:</td>
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
                        <td>Activity Note:</td>
                        <td>
                            <input
                                type="text"
                                value={note}
                                onChange={(e) => setNote(e.target.value)}
                                placeholder="e.g. Added 5"
                            />{' '}
                            <button type="submit">Submit Note</button>
                        </td>
                    </tr>
                </tbody>
            </table>
        </form>
    );
}

// Subcomponent 4: History list
function HistoryList({ history }) {
    return (
        <div>
            <h3>Activity History (List Rendering)</h3>
            {history.length === 0 ? (
                <p>No activity recorded yet.</p>
            ) : (
                <table border="1" cellPadding="5">
                    <thead>
                        <tr>
                            <th>#</th>
                            <th>Action</th>
                            <th>Value</th>
                            <th>Note</th>
                            <th>Time</th>
                        </tr>
                    </thead>
                    <tbody>
                        {history.map((item, idx) => (
                            <tr key={item.id}>
                                <td>{idx + 1}</td>
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

// Main Component for Practical 7
export default function Practical7_ReactCounterApp() {
    const [count, setCount] = useState(0);
    const [step, setStep] = useState(1);
    const [history, setHistory] = useState([]);

    const logHistory = (action, val, note) => {
        setHistory((prev) => [
            {
                id: Date.now() + Math.random(),
                action,
                value: val,
                note: note || '-',
                time: new Date().toLocaleTimeString(),
            },
            ...prev,
        ]);
    };

    const handleIncrement = () => {
        const next = count + step;
        setCount(next);
        logHistory('Increment', next, 'Added ' + step);
    };

    const handleDecrement = () => {
        const next = count - step;
        setCount(next);
        logHistory('Decrement', next, 'Subtracted ' + step);
    };

    const handleReset = () => {
        setCount(0);
        logHistory('Reset', 0, 'Reset to 0');
    };

    const handleAddNote = (note) => {
        logHistory('User Note', count, note);
    };

    return (
        <div>
            <h2>Practical 7: React Counter Application</h2>
            <p>Components, Conditional Rendering, List Rendering, Text Interpolation & Form Handling</p>
            <hr />

            <CounterDisplay count={count} />
            <br />
            <CounterControls
                onIncrement={handleIncrement}
                onDecrement={handleDecrement}
                onReset={handleReset}
                step={step}
            />
            <hr />
            <ConfigForm step={step} onStepChange={setStep} onAddNote={handleAddNote} />
            <hr />
            <HistoryList history={history} />
        </div>
    );
}
