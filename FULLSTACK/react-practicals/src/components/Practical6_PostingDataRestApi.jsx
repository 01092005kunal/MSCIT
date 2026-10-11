import React, { useState } from 'react';

export default function Practical6_PostingDataRestApi() {
    const [title, setTitle] = useState('');
    const [body, setBody] = useState('');
    const [userId, setUserId] = useState('1');
    const [loading, setLoading] = useState(false);
    const [statusMessage, setStatusMessage] = useState('');
    const [responseResult, setResponseResult] = useState(null);
    const [postsList, setPostsList] = useState([]);

    const handleSubmit = (e) => {
        e.preventDefault();
        if (!title.trim() || !body.trim()) {
            alert('Please fill all fields.');
            return;
        }

        setLoading(true);
        setStatusMessage('Posting data to REST API...');
        setResponseResult(null);

        fetch('https://jsonplaceholder.typicode.com/posts', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json; charset=UTF-8',
            },
            body: JSON.stringify({
                title: title,
                body: body,
                userId: Number(userId),
            }),
        })
            .then((res) => {
                if (!res.ok) throw new Error('Status: ' + res.status);
                return res.json();
            })
            .then((data) => {
                setLoading(false);
                setStatusMessage('Data posted successfully! (HTTP 201 Created)');
                setResponseResult(data);
                setPostsList([data, ...postsList]);
                setTitle('');
                setBody('');
            })
            .catch((err) => {
                setLoading(false);
                setStatusMessage('Error: ' + err.message);
            });
    };

    return (
        <div>
            <h2>Practical 6: Posting Data to REST API (React)</h2>
            <p>HTTP POST request with Controlled Form</p>
            <hr />

            <h3>Create New Post</h3>
            <form onSubmit={handleSubmit}>
                <table>
                    <tbody>
                        <tr>
                            <td>User ID:</td>
                            <td>
                                <input
                                    type="number"
                                    value={userId}
                                    onChange={(e) => setUserId(e.target.value)}
                                    min="1"
                                />
                            </td>
                        </tr>
                        <tr>
                            <td>Post Title:</td>
                            <td>
                                <input
                                    type="text"
                                    value={title}
                                    onChange={(e) => setTitle(e.target.value)}
                                    placeholder="Enter title"
                                    size="40"
                                />
                            </td>
                        </tr>
                        <tr>
                            <td>Post Body:</td>
                            <td>
                                <textarea
                                    value={body}
                                    onChange={(e) => setBody(e.target.value)}
                                    placeholder="Enter body content"
                                    rows="4"
                                    cols="42"
                                />
                            </td>
                        </tr>
                        <tr>
                            <td></td>
                            <td>
                                <button type="submit" disabled={loading}>
                                    {loading ? 'Submitting...' : 'Post Data (Submit)'}
                                </button>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </form>

            <br />
            {statusMessage && <p><b>{statusMessage}</b></p>}

            {responseResult && (
                <div>
                    <hr />
                    <h3>API Response Received:</h3>
                    <pre style={{ background: '#eee', padding: '10px' }}>
                        {JSON.stringify(responseResult, null, 2)}
                    </pre>
                </div>
            )}

            {postsList.length > 0 && (
                <div>
                    <hr />
                    <h3>Recently Submitted Posts:</h3>
                    <table border="1" cellPadding="5">
                        <thead>
                            <tr>
                                <th>Assigned ID</th>
                                <th>Title</th>
                                <th>Body</th>
                                <th>User ID</th>
                            </tr>
                        </thead>
                        <tbody>
                            {postsList.map((post, idx) => (
                                <tr key={idx}>
                                    <td>{post.id}</td>
                                    <td>{post.title}</td>
                                    <td>{post.body}</td>
                                    <td>{post.userId}</td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                </div>
            )}
        </div>
    );
}
