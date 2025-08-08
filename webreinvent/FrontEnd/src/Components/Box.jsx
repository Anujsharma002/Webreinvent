import React, { useEffect, useRef, useState } from 'react';
import './Box.css';

const Box = () => {
  const vantaRef = useRef(null);
  const [vantaEffect, setVantaEffect] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  async function handleClick() {
    const text = document.getElementById("keyword").value.trim();
    if (!text) return;

    setLoading(true);
    try {
      const response = await fetch("http://127.0.0.1:8000/analyze-keyword/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ keyword: text }),
      });

      const data = await response.json();
      const parsedResult = JSON.parse(data.result); 
      setResult(parsedResult);
    } catch (error) {
      console.error("Failed to fetch or parse data:", error);
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    if (!vantaEffect && window.VANTA && window.VANTA.GLOBE) {
      setVantaEffect(
        window.VANTA.GLOBE({
          el: vantaRef.current,
          mouseControls: true,
          touchControls: true,
          gyroControls: false,
          minHeight: 200.0,
          minWidth: 200.0,
          scale: 1.0,
          scaleMobile: 1.0,
          color: 0x0,
          backgroundColor: 0xd8d8ed,
        })
      );
    }

    return () => {
      if (vantaEffect) vantaEffect.destroy();
    };
  }, [vantaEffect]);

  return (
    <div ref={vantaRef} style={{ width: '100%', minHeight: '100vh', position: 'relative' }}>
      <div >
        {!result ? (
          <div className="container">
            <div className="container3">
            <h2>WebReinvent SEO Ranking</h2>
            <div>
              <input type="text" id="keyword" placeholder="Enter keyword for SEO search" />
              <button onClick={handleClick} disabled={loading}>
                {loading ? 'Searching...' : 'Search'}
              </button>
            </div>
            </div>
          </div>
        ) : (
          <div className="result container2">
            <h2>Search Results for: <i>{result.keyword}</i></h2>

            {/* WebReinvent Rank Info */}
            {result.webreinvent && (
              <>
                <h3>WebReinvent</h3>
                <table>
                  <thead>
                    <tr>
                      <th>Position</th>
                      <th>Title</th>
                      <th>URL</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>{result.webreinvent.position || 'Not Found'}</td>
                      <td>{result.webreinvent.title || 'N/A'}</td>
                      <td>
                        {result.webreinvent.url ? (
                          <a href={result.webreinvent.url} target="_blank" rel="noopener noreferrer">
                            {result.webreinvent.url}
                          </a>
                        ) : 'N/A'}
                      </td>
                    </tr>
                  </tbody>
                </table>
              </>
            )}

            {/* Competitors Info */}
            {Array.isArray(result.competitors) && result.competitors.length > 0 && (
              <>
                <h3>Top Competitors</h3>
                <table>
                  <thead>
                    <tr>
                      <th>Position</th>
                      <th>Title</th>
                      <th>URL</th>
                      <th>Description</th>
                      <th>Authority</th>
                      <th>SEO Notes</th>
                    </tr>
                  </thead>
                  <tbody>
                    {result.competitors.map((comp, index) => (
                      <tr key={index}>
                        <td>{comp.position || '-'}</td>
                        <td>{comp.title || '-'}</td>
                        <td>
                          <a href={comp.url} target="_blank" rel="noopener noreferrer">
                            {comp.url}
                          </a>
                        </td>
                        <td>{comp.meta_description || '-'}</td>
                        <td>{comp.domain_authority || '-'}</td>
                        <td>{comp.seo_notes || '-'}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </>
            )}

            {/* SEO Recommendations */}
            {Array.isArray(result.seo_recommendations) && result.seo_recommendations.length > 0 && (
              <>
                <h3>SEO Recommendations</h3>
                <ul>
                  {result.seo_recommendations.map((note, index) => (
                    <li key={index}>{note}</li>
                  ))}
                </ul>
              </>
            )}
          </div>
        )}
      </div>
    </div>
  );
};

export default Box;
