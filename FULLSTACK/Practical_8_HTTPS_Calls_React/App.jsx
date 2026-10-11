// App.jsx - Practical 8: HTTPS Calls in React Component
// Demonstrates secure HTTPS REST API communication using async/await,
// error handling, search filter, and state management in a React component.

function App() {
    const [posts, setPosts] = React.useState([]);
    const [filteredPosts, setFilteredPosts] = React.useState([]);
    const [searchTerm, setSearchTerm] = React.useState('');
    const [limit, setLimit] = React.useState(5);
    const [loading, setLoading] = React.useState(false);
    const [error, setError] = React.useState(null);

    // Secure HTTPS request using async / await
    const fetchHttpsData = async (countLimit) => {
        setLoading(true);
        setError(null);

        try {
            // Secure HTTPS endpoint
            const url = `https://jsonplaceholder.typicode.com/posts?_limit=${countLimit || limit}`;
            const response = await fetch(url);

            if (!response.ok) {
                throw new Error(`HTTPS Request failed! Status: ${response.status} (${response.statusText})`);
            }

            const data = await response.json();
            setPosts(data);
            setFilteredPosts(data);
        } catch (err) {
            setError(err.message || 'Failed to fetch data from HTTPS endpoint.');
        } finally {
            setLoading(false);
        }
    };

    // Trigger HTTPS call on component mount and when limit changes
    React.useEffect(() => {
        fetchHttpsData(limit);
    }, [limit]);

    // Handle Search filter
    const handleSearch = (e) => {
        const query = e.target.value;
        setSearchTerm(query);

        if (!query.trim()) {
            setFilteredPosts(posts);
        } else {
            const filtered = posts.filter((post) =>
                post.title.toLowerCase().includes(query.toLowerCase())
            );
            setFilteredPosts(filtered);
        }
    };

    return (
        <div>
            <h1>Practical 8: HTTPS Calls in React Component</h1>
            <p>Demonstrating Secure HTTPS API communication, Async/Await, Error Handling & Filter</p>
            <hr />

            {/* Controls */}
            <table>
                <tbody>
                    <tr>
                        <td>Fetch Records Count:</td>
                        <td>
                            <select value={limit} onChange={(e) => setLimit(Number(e.target.value))}>
                                <option value="5">5 records</option>
                                <option value="10">10 records</option>
                                <option value="15">15 records</option>
                            </select>
                            {' '}
                            <button onClick={() => fetchHttpsData(limit)}>Reload HTTPS Call</button>
                        </td>
                    </tr>
                    <tr>
                        <td>Search / Filter by Title:</td>
                        <td>
                            <input
                                type="text"
                                value={searchTerm}
                                onChange={handleSearch}
                                placeholder="Filter fetched posts..."
                                size="30"
                            />
                        </td>
                    </tr>
                </tbody>
            </table>

            <br />

            {/* State Handling: Loading, Error, and Results */}
            {loading && <p><b>[HTTPS Status] Connecting to secure endpoint and fetching data...</b></p>}
            
            {error && (
                <div>
                    <p style={{ color: 'red' }}><b>[HTTPS Error]: {error}</b></p>
                    <button onClick={() => fetchHttpsData(limit)}>Retry Request</button>
                </div>
            )}

            {!loading && !error && (
                <div>
                    <h3>Fetched Results ({filteredPosts.length} of {posts.length} shown)</h3>
                    {filteredPosts.length === 0 ? (
                        <p>No matching records found.</p>
                    ) : (
                        <table border="1" cellPadding="5">
                            <thead>
                                <tr>
                                    <th>Post ID</th>
                                    <th>User ID</th>
                                    <th>Title</th>
                                    <th>Body</th>
                                </tr>
                            </thead>
                            <tbody>
                                {filteredPosts.map((post) => (
                                    <tr key={post.id}>
                                        <td>{post.id}</td>
                                        <td>{post.userId}</td>
                                        <td><b>{post.title}</b></td>
                                        <td>{post.body}</td>
                                    </tr>
                                ))}
                            </tbody>
                        </table>
                    )}
                </div>
            )}
        </div>
    );
}
