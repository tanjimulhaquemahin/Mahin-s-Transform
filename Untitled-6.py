:root {
  --bg: #0b0d12;
  --panel: #12151c;
  --border: #232834;
  --text: #e8eaf0;
  --muted: #8a92a6;
  --accent: #7c5cff;
}

* { box-sizing: border-box; margin: 0; padding: 0; }

html, body {
  height: 100%;
  background: var(--bg);
  color: var(--text);
  font-family: Inter, system-ui, -apple-system, "Segoe UI", sans-serif;
}

.app { display: grid; grid-template-columns: 380px 1fr; height: 100vh; }

.panel {
  background: var(--panel);
  border-right: 1px solid var(--border);
  padding: 24px;
  overflow-y: auto;
}

.brand { font-size: 22px; margin-bottom: 20px; }
.brand span { color: var(--accent); }

.group { padding: 16px 0; border-top: 1px solid var(--border); }
.group h2 { font-size: 13px; text-transform: uppercase; letter-spacing: .08em; color: var(--muted); margin-bottom: 12px; }

input[type="file"] { width: 100%; font-size: 13px; color: var(--muted); }
input[type="file"]::file-selector-button {
  background: #1c2130; color: var(--text); border: 1px solid var(--border);
  padding: 8px 12px; border-radius: 8px; margin-right: 10px; cursor: pointer;
}

textarea {
  width: 100%; background: #0d1017; color: var(--text);
  border: 1px solid var(--border); border-radius: 10px; padding: 10px;
  font: inherit; resize: vertical;
}
textarea:focus { outline: 1px solid var(--accent); }

.emojiRow { display: flex; flex-wrap: wrap; gap: 6px; margin: 10px 0 4px; }
.emojiBtn {
  background: #1c2130; border: 1px solid var(--border); border-radius: 8px;
  padding: 4px 8px; font-size: 18px; cursor: pointer;
}
.emojiBtn:hover { border-color: var(--accent); }

.hint { font-size: 12px; color: var(--muted); margin: 8px 0; }
kbd { background: #1c2130; border-radius: 4px; padding: 1px 5px; font-size: 11px; }

.field { display: block; margin-top: 12px; }
.fieldLabel { display: flex; justify-content: space-between; font-size: 13px; margin-bottom: 6px; }
.fieldLabel b { color: var(--accent); font-weight: 600; }
input[type="range"] { width: 100%; accent-color: var(--accent); }

.stage {
  display: flex; align-items: center; justify-content: center;
  padding: 24px; min-height: 0;
  background: radial-gradient(circle at 50% 30%, #161a26, var(--bg));
}
.previewWrap { display: flex; flex-direction: column; align-items: center; gap: 14px; height: 100%; }
.canvas {
  height: calc(100vh - 120px);
  aspect-ratio: 9 / 16;
  border-radius: 14px;
  border: 1px solid var(--border);
  box-shadow: 0 20px 60px rgba(0,0,0,.6);
}
.hiddenVideo { position: absolute; width: 1px; height: 1px; opacity: 0; pointer-events: none; }

.btn {
  background: var(--accent); color: white; border: 0; border-radius: 10px;
  padding: 10px 18px; font-weight: 600; cursor: pointer;
}
.btn:disabled { opacity: .4; cursor: not-allowed; }