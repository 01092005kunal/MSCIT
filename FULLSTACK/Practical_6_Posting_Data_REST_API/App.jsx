// App.jsx - Practical 6: Posting data to REST API
// Demonstrates HTTP POST request using fetch() with controlled form in React

function App() {
    const [title, setTitle] = React.useState('');
    const [body, setBody] = React.useState('');
    const [userId, setUserId] = React.useState('1');

    const [loading, setLoading] = React.useState(false);
    const [statusMessage, setStatusMessage] = React.useState('');
    const [responseResult, setResponseResult] = React.useState(null);
    const [postsList, setPostsList] = React.useState([]);

    const handleSubmit = (e) => {
        e.preventDefault();

        if (!title.trim() || !body.trim()) {
            alert('Please fill all fields.');
            return;
        }

        setLoading(true);
        setStatusMessage('Sending POST request...');
        setResponseResult(null);

        // Making HTTP POST call to REST API
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
                if (!res.ok) {
                    throw new Error('Server returned status: ' + res.status);
                }
                return res.json();
            })
            .then((data) => {
                setLoading(false);
                setStatusMessage('Data posted successfully! (HTTP Status: 201 Created)');
                setResponseResult(data);
                // Append newly posted item to list
                setPostsList([data, ...postsList]);
                // Clear form
                setTitle('');
                setBody('');
            })
            .catch((err) => {
                setLoading(false);
                setStatusMessage('Error posting data: ' + err.message);
            });
    };

    return (
        <div>
            <h1>Practical 6: Posting Data to REST API (React)</h1>
            <p>Demonstrating HTTP POST Request with Controlled Form</p>
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

            {/* Response Details from REST API */}
            {responseResult && (
                <div>
                    <hr />
                    <h3>API Response Received:</h3>
                    <pre style={{ background: '#eee', padding: '10px' }}>
                        {JSON.stringify(responseResult, null, 2)}
                    </pre>
                </div>
            )}

            {/* Submitted Posts List */}
            {postsList.length > 0 && (
                <div>
                    <hr />
                    <h3>Recently Submitted Posts ({postsList.length}):</h3>
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
