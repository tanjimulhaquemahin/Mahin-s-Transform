"use client";

import { ChangeEvent } from "react";
import { Settings } from "@/lib/settings";

type Props = {
  settings: Settings;
  onChange: (patch: Partial<Settings>) => void;
  onVideo: (file: File) => void;
  onLogo: (file: File) => void;
  videoName?: string;
  logoName?: string;
};

const QUICK_EMOJIS = ["🔥", "😱", "💡", "🚀", "👀", "✅", "💰", "⚡"];

function Slider(props: {
  label: string;
  value: number;
  min: number;
  max: number;
  onChange: (v: number) => void;
}) {
  return (
    <label className="field">
      <span className="fieldLabel">
        {props.label} <b>{props.value}</b>
      </span>
      <input
        type="range"
        min={props.min}
        max={props.max}
        value={props.value}
        onChange={(e) => props.onChange(Number(e.target.value))}
      />
    </label>
  );
}

export default function Controls({
  settings,
  onChange,
  onVideo,
  onLogo,
  videoName,
  logoName,
}: Props) {
  const pick =
    (cb: (f: File) => void) => (e: ChangeEvent<HTMLInputElement>) => {
      const file = e.target.files?.[0];
      if (file) cb(file);
    };

  return (
    <aside className="panel">
      <h1 className="brand">CineAuto <span>Studio</span></h1>

      <section className="group">
        <h2>1. Video</h2>
        <input type="file" accept="video/*" onChange={pick(onVideo)} />
        {videoName && <p className="hint">{videoName}</p>}
      </section>

      <section className="group">
        <h2>2. Headline</h2>
        <textarea
          rows={3}
          value={settings.headline}
          onChange={(e) => onChange({ headline: e.target.value })}
          placeholder="Type your headline 🔥"
        />
        <div className="emojiRow">
          {QUICK_EMOJIS.map((em) => (
            <button
              key={em}
              className="emojiBtn"
              onClick={() => onChange({ headline: settings.headline + em })}
            >
              {em}
            </button>
          ))}
        </div>
        <p className="hint">
          Tip: Windows <kbd>Win</kbd>+<kbd>.</kbd> · Mac <kbd>Ctrl</kbd>+<kbd>Cmd</kbd>+<kbd>Space</kbd> opens the emoji picker.
        </p>
        <Slider label="Font size" value={settings.fontSize} min={30} max={140}
          onChange={(v) => onChange({ fontSize: v })} />
        <Slider label="Distance from top" value={settings.headlineTop} min={0} max={600}
          onChange={(v) => onChange({ headlineTop: v })} />
      </section>

      <section className="group">
        <h2>3. Logo (transparent PNG)</h2>
        <input type="file" accept="image/png" onChange={pick(onLogo)} />
        {logoName && <p className="hint">{logoName}</p>}
        <Slider label="Logo width" value={settings.logoWidth} min={60} max={800}
          onChange={(v) => onChange({ logoWidth: v })} />
        <Slider label="Distance from bottom" value={settings.logoBottom} min={0} max={500}
          onChange={(v) => onChange({ logoBottom: v })} />
      </section>

      <section className="group">
        <h2>4. Video layout</h2>
        <Slider label="Video width" value={settings.videoWidth} min={400} max={1080}
          onChange={(v) => onChange({ videoWidth: v })} />
        <Slider label="Vertical offset" value={settings.videoOffsetY} min={-500} max={500}
          onChange={(v) => onChange({ videoOffsetY: v })} />
        <Slider label="Corner radius" value={settings.cornerRadius} min={0} max={200}
          onChange={(v) => onChange({ cornerRadius: v })} />
      </section>
    </aside>
  );
}