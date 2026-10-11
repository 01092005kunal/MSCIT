// App.jsx - Practical 5: HTTP calls using REST API
// Fetches data using native fetch API and displays in React component

function App() {
    const [users, setUsers] = React.useState([]);
    const [loading, setLoading] = React.useState(false);
    const [error, setError] = React.useState(null);

    // Function to fetch data from REST API
    const fetchUsers = () => {
        setLoading(true);
        setError(null);

        fetch('https://jsonplaceholder.typicode.com/users')
            .then((response) => {
                if (!response.ok) {
                    throw new Error('HTTP error! Status: ' + response.status);
                }
                return response.json();
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

    // Fetch on initial component mount
    React.useEffect(() => {
        fetchUsers();
    }, []);

    return (
        <div>
            <h1>Practical 5: HTTP Calls using REST API (React)</h1>
            <p>Demonstrating HTTP GET Request using fetch() and useEffect</p>
            <hr />

            <button onClick={fetchUsers}>Refresh / Fetch Data</button>
            <br /><br />

            {/* Conditional display based on request state */}
            {loading && <p><b>Loading data from API... Please wait.</b></p>}
            {error && <p style={{ color: 'red' }}><b>Error: {error}</b></p>}

            {!loading && !error && (
                <div>
                    <h3>Users List ({users.length} records fetched)</h3>
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
