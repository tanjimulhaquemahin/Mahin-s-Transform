"use client";

import { useEffect, useState } from "react";
import Controls from "@/components/Controls";
import PreviewCanvas from "@/components/PreviewCanvas";
import { DEFAULT_SETTINGS, Settings } from "@/lib/settings";

export default function Home() {
  const [settings, setSettings] = useState<Settings>(DEFAULT_SETTINGS);
  const [videoFile, setVideoFile] = useState<File | null>(null);
  const [logoFile, setLogoFile] = useState<File | null>(null);
  const [videoUrl, setVideoUrl] = useState<string | null>(null);
  const [logoUrl, setLogoUrl] = useState<string | null>(null);

  // Turn uploaded files into temporary URLs the browser can display
  useEffect(() => {
    if (!videoFile) return;
    const url = URL.createObjectURL(videoFile);
    setVideoUrl(url);
    return () => URL.revokeObjectURL(url);
  }, [videoFile]);

  useEffect(() => {
    if (!logoFile) return;
    const url = URL.createObjectURL(logoFile);
    setLogoUrl(url);
    return () => URL.revokeObjectURL(url);
  }, [logoFile]);

  return (
    <main className="app">
      <Controls
        settings={settings}
        onChange={(patch) => setSettings((s) => ({ ...s, ...patch }))}
        onVideo={setVideoFile}
        onLogo={setLogoFile}
        videoName={videoFile?.name}
        logoName={logoFile?.name}
      />
      <section className="stage">
        <PreviewCanvas settings={settings} videoUrl={videoUrl} logoUrl={logoUrl} />
      </section>
    </main>
  );
}