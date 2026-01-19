import React from 'react';
import { motion } from 'framer-motion';
import { FileText, CheckCircle, Clock, Loader2, Download } from 'lucide-react';

const JobCard = ({ job }) => {
    const isCompleted = job.status === 'Completed';

    return (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            className="glass-card p-6 rounded-xl w-full mb-4 border-l-4 border-l-blue-500"
        >
            <div className="flex justify-between items-start">
                <div>
                    <div className="flex items-center gap-2 mb-2">
                        <h3 className="text-lg font-bold text-white flex items-center gap-2">
                            <FileText className="w-5 h-5 text-blue-400" />
                            Job #{job.id}
                        </h3>
                        <span className={`px-2 py-1 rounded-full text-xs font-semibold flex items-center gap-1
              ${isCompleted ? 'bg-green-500/20 text-green-400' : 'bg-yellow-500/20 text-yellow-400'}`}>
                            {isCompleted ? <CheckCircle className="w-3 h-3" /> : <Loader2 className="w-3 h-3 animate-spin" />}
                            {job.status}
                        </span>
                    </div>
                    <p className="text-slate-400 text-sm">
                        Created: {new Date(job.created_at).toLocaleString()}
                    </p>
                </div>
            </div>

            {isCompleted && job.pdf_files && job.pdf_files.length > 0 && (
                <motion.div
                    initial={{ height: 0, opacity: 0 }}
                    animate={{ height: 'auto', opacity: 1 }}
                    className="mt-4 pt-4 border-t border-slate-700/50"
                >
                    <p className="text-sm font-semibold text-slate-300 mb-2">Generated Files:</p>
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-2">
                        {job.pdf_files.map((url, idx) => (
                            <a
                                key={idx}
                                href={url}
                                target="_blank"
                                rel="noopener noreferrer"
                                className="flex items-center gap-2 p-2 rounded-lg bg-slate-800/50 hover:bg-blue-600/20 text-sm text-slate-200 transition-colors group"
                            >
                                <Download className="w-4 h-4 text-slate-400 group-hover:text-blue-400" />
                                <span className="truncate">Document_{idx + 1}.pdf</span>
                            </a>
                        ))}
                    </div>
                </motion.div>
            )}
        </motion.div>
    );
};

export default JobCard;
