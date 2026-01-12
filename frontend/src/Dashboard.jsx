import React, { useEffect, useState } from "react";

// Minimal charting without heavy libraries
const MetricCard = ({ title, value }) => (
  <div className="bg-white shadow-md rounded-lg p-4 m-2 w-40 text-center">
    <h2 className="text-gray-700 font-semibold">{title}</h2>
    <p className="text-3xl font-bold text-indigo-600">{value}</p>
  </div>
);

const Dashboard = () => {
  const [metrics, setMetrics] = useState({});
  const [loading, setLoading] = useState(true);
  const campaignId = 1; // demo campaign

  useEffect(() => {
    const fetchMetrics = async () => {
      try {
        const res = await fetch(`/api/analytics/campaigns/${campaignId}`);
        const data = await res.json();
        setMetrics(data.metrics || {});
      } catch (err) {
        console.error("Failed to fetch metrics", err);
      } finally {
        setLoading(false);
      }
    };
    fetchMetrics();
  }, []);

  if (loading) return <p className="text-gray-500 p-4">Loading metrics...</p>;

  return (
    <div className="p-6 bg-gray-100 min-h-screen">
      <h1 className="text-2xl font-bold mb-4 text-indigo-700">Go Phish Telemetry Dashboard</h1>
      <div className="flex flex-wrap">
        {Object.entries(metrics).map(([eventType, count]) => (
          <MetricCard key={eventType} title={eventType} value={count} />
        ))}
      </div>
    </div>
  );
};

export default Dashboard;
