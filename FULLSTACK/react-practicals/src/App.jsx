import React, { useState } from 'react';
import Practical5_HttpRestApi from './components/Practical5_HttpRestApi';
import Practical6_PostingDataRestApi from './components/Practical6_PostingDataRestApi';
import Practical7_ReactCounterApp from './components/Practical7_ReactCounterApp';
import Practical8_HttpsCallsReact from './components/Practical8_HttpsCallsReact';

export default function App() {
    const [activeTab, setActiveTab] = useState(5);

    return (
        <div>
            <h1>React Practicals (Practicals 5 to 8)</h1>
            <p>Ruia College MSc IT - Full Stack Practical</p>
            <hr />

            {/* Simple raw buttons to switch practicals */}
            <div>
                <b>Select Practical: </b>
                <button onClick={() => setActiveTab(5)} disabled={activeTab === 5}>Practical 5 (HTTP Calls)</button>{' '}
                <button onClick={() => setActiveTab(6)} disabled={activeTab === 6}>Practical 6 (Posting Data)</button>{' '}
                <button onClick={() => setActiveTab(7)} disabled={activeTab === 7}>Practical 7 (Counter App)</button>{' '}
                <button onClick={() => setActiveTab(8)} disabled={activeTab === 8}>Practical 8 (HTTPS Calls)</button>
            </div>
            <hr />

            {/* Display selected practical component */}
            {activeTab === 5 && <Practical5_HttpRestApi />}
            {activeTab === 6 && <Practical6_PostingDataRestApi />}
            {activeTab === 7 && <Practical7_ReactCounterApp />}
            {activeTab === 8 && <Practical8_HttpsCallsReact />}
        </div>
    );
}
