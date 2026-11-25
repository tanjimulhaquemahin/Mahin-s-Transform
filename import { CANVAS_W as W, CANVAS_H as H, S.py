"use client";

import { useEffect, useRef, useState } from "react";
import { CANVAS_H, CANVAS_W, Settings } from "@/lib/settings";
import { drawFrame } from "@/lib/drawFrame";

type Props = {
  settings: Settings;
  videoUrl: string | null;
  logoUrl: string | null;
};

export default function PreviewCanvas({ settings, videoUrl, logoUrl }: Props) {
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const videoRef = useRef<HTMLVideoElement>(null);
  const logoRef = useRef<HTMLImageElement | null>(null);
  const settingsRef = useRef(settings);
  const [playing, setPlaying] = useState(false);

  // Keep the latest settings available to the drawing loop
  useEffect(() => {
    settingsRef.current = settings;
  }, [settings]);

  // Load the logo image whenever a new one is uploaded
  useEffect(() => {
    if (!logoUrl) {
      logoRef.current = null;
      return;
    }
    const img = new Image();
    img.onload = () => {
      logoRef.current = img;
    };
    img.src = logoUrl;
  }, [logoUrl]);

  // Redraw the canvas continuously (this is what makes video play in the preview)
  useEffect(() => {
    const ctx = canvasRef.current!.getContext("2d")!;
    let id = 0;
    const loop = () => {
      drawFrame(ctx, settingsRef.current, videoRef.current, logoRef.current);
      id = requestAnimationFrame(loop);
    };
    loop();
    return () => cancelAnimationFrame(id);
  }, []);

  const togglePlay = () => {
    const v = videoRef.current;
    if (!v || !videoUrl) return;
    if (v.paused) v.play();
    else v.pause();
  };

  return (
    <div className="previewWrap">
      <canvas
        ref={canvasRef}
        width={CANVAS_W}
        height={CANVAS_H}
        className="canvas"
      />
      <video
        ref={videoRef}
        src={videoUrl ?? undefined}
        className="hiddenVideo"
        loop
        playsInline
        onPlay={() => setPlaying(true)}
        onPause={() => setPlaying(false)}
      />
      <button className="btn" onClick={togglePlay} disabled={!videoUrl}>
        {playing ? "⏸ Pause" : "▶ Play preview"}
      </button>
    </div>
  );
}