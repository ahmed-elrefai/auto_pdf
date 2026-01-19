import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { motion } from 'framer-motion';
import { Zap } from 'lucide-react';
import UploadZone from './components/UploadZone';
import JobCard from './components/ui/JobCard';

function App() {
  const [jobs, setJobs] = useState([]);
  const [loading, setLoading] = useState(true);

  const fetchJobs = async () => {
    try {
      const response = await axios.get('http://localhost:8000/api/jobs/');
      setJobs(response.data);
    } catch (error) {
      console.error("Error fetching jobs:", error);
    } finally {
      setLoading(false);
    }
  };

  // Initial fetch
  useEffect(() => {
    fetchJobs();
  }, []);

  // Polling every 2 seconds
  useEffect(() => {
    const interval = setInterval(() => {
      // Optimistically update only if we have jobs or expecting them
      fetchJobs();
    }, 2000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="min-h-screen relative p-4 md:p-8">
      {/* Background Elements */}
      <div className="fixed top-0 left-0 w-full h-full overflow-hidden -z-10 pointer-events-none">
        <div className="absolute top-[-10%] left-[-10%] w-[40%] h-[40%] bg-blue-500/10 rounded-full blur-[100px] animate-float" />
        <div className="absolute bottom-[-10%] right-[-10%] w-[40%] h-[40%] bg-purple-500/10 rounded-full blur-[100px] animate-float" style={{ animationDelay: '2s' }} />
      </div>

      <div className="max-w-4xl mx-auto">
        <header className="mb-8 flex items-center justify-between">
          <motion.div
            initial={{ opacity: 0, x: -20 }}
            animate={{ opacity: 1, x: 0 }}
            className="flex items-center gap-3"
          >
            <div className="p-2 bg-gradient-to-r from-blue-600 to-purple-600 rounded-lg shadow-lg">
              <Zap className="w-6 h-6 text-white" />
            </div>
            <h1 className="text-3xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-white to-slate-400">
              auto_pdf
            </h1>
          </motion.div>

          <div className="text-sm text-slate-400">
            {jobs.length} Jobs Processed
          </div>
        </header>

        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.1 }}
        >
          <UploadZone onUploadSuccess={fetchJobs} />
        </motion.div>

        <section>
          <h2 className="text-xl font-semibold text-slate-200 mb-4 px-2">Recent Activity</h2>

          {loading && jobs.length === 0 ? (
            <div className="text-center py-10 text-slate-500">Loading jobs...</div>
          ) : (
            <div className="space-y-4">
              {jobs.map((job) => (
                <JobCard key={job.id} job={job} />
              ))}
              {jobs.length === 0 && (
                <div className="text-center py-12 glass-card rounded-xl text-slate-400">
                  No jobs yet. Upload a CSV to get started!
                </div>
              )}
            </div>
          )}
        </section>
      </div>
    </div>
  );
}

export default App;
