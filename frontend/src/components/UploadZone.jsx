import React, { useState } from 'react';
import axios from 'axios';
import { Upload, FileUp, Loader2 } from 'lucide-react';

const UploadZone = ({ onUploadSuccess }) => {
    const [isUploading, setIsUploading] = useState(false);
    const [error, setError] = useState(null);

    const handleUpload = async (event) => {
        event.preventDefault();
        setIsUploading(true);
        setError(null);

        const formData = new FormData(event.target);

        // Validate CSV presence
        if (!formData.get('csv_file').name) {
            setError("Please select a CSV file.");
            setIsUploading(false);
            return;
        }

        try {
            await axios.post('http://localhost:8000/api/jobs/', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                    // Add Authorization header here if needed later
                }
            });
            // Clear form
            event.target.reset();
            onUploadSuccess();
        } catch (err) {
            console.error(err);
            setError("Upload failed. Please try again.");
        } finally {
            setIsUploading(false);
        }
    };

    return (
        <div className="glass-card p-8 rounded-xl mb-8">
            <h2 className="text-2xl font-bold mb-6 text-white flex items-center gap-2">
                <Upload className="w-6 h-6 text-blue-400" />
                New Job
            </h2>

            <form onSubmit={handleUpload} className="flex flex-col gap-4">
                <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                    {/* CSV Input */}
                    <div>
                        <label className="block text-sm font-medium text-slate-300 mb-2">CSV Data File</label>
                        <div className="relative group">
                            <div className="absolute inset-0 bg-blue-500/10 rounded-lg group-hover:bg-blue-500/20 transition-colors" />
                            <input
                                type="file"
                                name="csv_file"
                                accept=".csv"
                                className="relative block w-full text-sm text-slate-300
                        file:mr-4 file:py-3 file:px-4
                        file:rounded-l-lg file:border-0
                        file:text-sm file:font-semibold
                        file:bg-blue-600 file:text-white
                        hover:file:bg-blue-700
                        cursor-pointer border border-slate-700 rounded-lg"
                            />
                        </div>
                    </div>

                    {/* Template Input */}
                    <div>
                        <label className="block text-sm font-medium text-slate-300 mb-2">HTML Template (Optional)</label>
                        <div className="relative group">
                            <div className="absolute inset-0 bg-purple-500/10 rounded-lg group-hover:bg-purple-500/20 transition-colors" />
                            <input
                                type="file"
                                name="template_file"
                                accept=".html"
                                className="relative block w-full text-sm text-slate-300
                        file:mr-4 file:py-3 file:px-4
                        file:rounded-l-lg file:border-0
                        file:text-sm file:font-semibold
                        file:bg-purple-600 file:text-white
                        hover:file:bg-purple-700
                        cursor-pointer border border-slate-700 rounded-lg"
                            />
                        </div>
                    </div>
                </div>

                {error && (
                    <div className="p-3 bg-red-500/20 text-red-300 rounded-lg border border-red-500/30 text-sm">
                        {error}
                    </div>
                )}

                <div className="mt-4 flex justify-end">
                    <button
                        type="submit"
                        disabled={isUploading}
                        className="bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-700 hover:to-purple-700 
                text-white font-bold py-3 px-8 rounded-lg transition-all transform hover:scale-105
                disabled:opacity-50 disabled:cursor-not-allowed flex items-center gap-2"
                    >
                        {isUploading ? (
                            <>
                                <Loader2 className="w-5 h-5 animate-spin" />
                                Uploading...
                            </>
                        ) : (
                            <>
                                <FileUp className="w-5 h-5" />
                                Start Generation
                            </>
                        )}
                    </button>
                </div>
            </form>
        </div>
    );
};

export default UploadZone;
