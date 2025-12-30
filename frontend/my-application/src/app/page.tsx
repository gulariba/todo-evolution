"use client";

import { useEffect, useState } from "react";

export default function Home() {
  const [status, setStatus] = useState("Checking backend...");

  useEffect(() => {
    fetch(`${process.env.NEXT_PUBLIC_API_URL}/docs`)
      .then(() => setStatus("✅ Backend connected"))
      .catch(() => setStatus("❌ Backend not reachable"));
  }, []);

  return (
    <main style={{ padding: 40 }}>
      <h1>Todo Evolution</h1>
      <p>{status}</p>
    </main>
  );
}

