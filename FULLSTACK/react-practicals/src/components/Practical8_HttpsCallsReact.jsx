import React, { useState, useEffect } from 'react';

export default function Practical8_HttpsCallsReact() {
    const [posts, setPosts] = useState([]);
    const [filteredPosts, setFilteredPosts] = useState([]);
    const [searchTerm, setSearchTerm] = useState('');
    const [limit, setLimit] = useState(5);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    const fetchHttpsData = async (countLimit) => {
        setLoading(true);
        setError(null);

        try {
            const url = `https://jsonplaceholder.typicode.com/posts?_limit=${countLimit || limit}`;
            const response = await fetch(url);

            if (!response.ok) {
                throw new Error(`HTTPS Request failed! Status: ${response.status}`);
            }

            const data = await response.json();
            setPosts(data);
            setFilteredPosts(data);
        } catch (err) {
            setError(err.message || 'HTTPS request failed');
        } finally {
            setLoading(false);
        }
    };

    useEffect(() => {
        fetchHttpsData(limit);
    }, [limit]);

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
            <h2>Practical 8: HTTPS Calls in React Component</h2>
            <p>Secure HTTPS endpoint with async/await, error handling & live filter</p>
            <hr />

            <table>
                <tbody>
                    <tr>
                        <td>Fetch Records Count:</td>
                        <td>
                            <select value={limit} onChange={(e) => setLimit(Number(e.target.value))}>
                                <option value="5">5 records</option>
                                <option value="10">10 records</option>
                                <option value="15">15 records</option>
                            </select>{' '}
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
            {loading && <p><b>[HTTPS] Connecting to secure endpoint... Please wait.</b></p>}
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
