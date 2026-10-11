import React, { useState, useEffect } from 'react';

export default function Practical5_HttpRestApi() {
    const [users, setUsers] = useState([]);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    const fetchUsers = () => {
        setLoading(true);
        setError(null);

        fetch('https://jsonplaceholder.typicode.com/users')
            .then((res) => {
                if (!res.ok) throw new Error('HTTP status: ' + res.status);
                return res.json();
            })
            .then((data) => {
                setUsers(data);
                setLoading(false);
            })
            .catch((err) => {
                setError(err.message);
                setLoading(false);
            });
    };

    useEffect(() => {
        fetchUsers();
    }, []);

    return (
        <div>
            <h2>Practical 5: HTTP Calls using REST API (React)</h2>
            <p>HTTP GET request using fetch() and useEffect()</p>
            <hr />

            <button onClick={fetchUsers}>Refresh / Fetch Data</button>
            <br /><br />

            {loading && <p><b>Loading data from API... Please wait.</b></p>}
            {error && <p style={{ color: 'red' }}><b>Error: {error}</b></p>}

            {!loading && !error && (
                <div>
                    <h3>Users List ({users.length} records):</h3>
                    <table border="1" cellPadding="5">
                        <thead>
                            <tr>
                                <th>ID</th>
                                <th>Name</th>
                                <th>Email</th>
                                <th>Phone</th>
                                <th>Company</th>
                                <th>City</th>
                            </tr>
                        </thead>
                        <tbody>
                            {users.map((user) => (
                                <tr key={user.id}>
                                    <td>{user.id}</td>
                                    <td>{user.name}</td>
                                    <td>{user.email}</td>
                                    <td>{user.phone}</td>
                                    <td>{user.company.name}</td>
                                    <td>{user.address.city}</td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                </div>
            )}
        </div>
    );
}
