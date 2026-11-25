export const CANVAS_W = 1080;
export const CANVAS_H = 1920;

export type Settings = {
  headline: string;
  fontSize: number;
  headlineTop: number;   // distance from top (px)
  videoWidth: number;    // px, height follows the video's aspect ratio
  videoOffsetY: number;  // moves the video up/down from the exact middle
  cornerRadius: number;  // px
  logoWidth: number;     // px
  logoBottom: number;    // distance from bottom (px)
};

export const DEFAULT_SETTINGS: Settings = {
  headline: "Your headline here 🔥",
  fontSize: 72,
  headlineTop: 140,
  videoWidth: 1000,
  videoOffsetY: 0,
  cornerRadius: 40,
  logoWidth: 260,
  logoBottom: 120,
};
