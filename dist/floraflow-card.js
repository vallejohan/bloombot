const FLORA_ICONS = {
    tomato: "mdi:tomato",
    cucumber: "mdi:pickled-cucumber",
    carrot: "mdi:carrot",
    corn: "mdi:corn",
    chili: "mdi:chili-pepper",
    pepper: "mdi:chili-pepper",
    pumpkin: "mdi:pumpkin",
    squash: "mdi:pumpkin",
    sprout: "mdi:sprout",
    potato: "mdi:potato",
    mushroom: "mdi:mushroom",
    cabbage: "mdi:leafy-green",
    onion: "mdi:onion",
    garlic: "mdi:garlic",
    leaf: "mdi:leaf",
    flower: "mdi:flower",
    tree: "mdi:tree",
    pot: "mdi:pot",
    sprinkler: "mdi:sprinkler",
    pump: "mdi:water-pump",
    eggplant: "mdi:eggplant",
    broccoli: "mdi:broccoli",
    pea: "mdi:pea",
    radish: "mdi:sprout",
    apple: "mdi:apple",
    banana: "mdi:banana",
    cherry: "mdi:fruit-cherries",
    cherries: "mdi:fruit-cherries",
    grape: "mdi:fruit-grapes",
    grapes: "mdi:fruit-grapes",
    strawberry: "mdi:fruit-cherries",
    pear: "mdi:fruit-pear",
    citrus: "mdi:fruit-citrus",
    orange: "mdi:fruit-citrus",
    lemon: "mdi:fruit-citrus",
    pineapple: "mdi:fruit-pineapple",
    watermelon: "mdi:fruit-watermelon",
    melon: "mdi:fruit-watermelon",
    berry: "mdi:fruit-cherries",
    berries: "mdi:fruit-cherries"
};

const FLORA_SVGS = {
    tomato: '<circle cx="12" cy="13" r="7" /><path d="M12 3v3 M9 4.5l3 1.5 3-1.5 M10 6.5h4" />',
    cucumber: '<path d="M6 17c-1.5-1.5-1.5-4 0-5.5l8.5-8.5c1.5-1.5 4-1.5 5.5 0s1.5 4 0 5.5L11.5 17c-1.5 1.5-4 1.5-5.5 0z" /><path d="M9.5 13.5h.01 M12 11h.01 M14.5 8.5h.01" stroke-dasharray="0 0" stroke-width="3" stroke-linecap="round" />',
    carrot: '<path d="M18 4l2 2L10 18l-6 2 2-6Z" /><path d="M13 9l1-1 M10 12l1-1 M7 15l1-1" /><path d="M19 5l3-3 M19 5l1 3 M19 5l-3-1" />',
    corn: '<path d="M8 9c0-4 2-6 4-6s4 2 4 6v6c0 4-2 6-4 6s-4-2-4-6V9z" /><path d="M5 21c0-4 1-9 4-12" /><path d="M19 21c0-4-1-9-4-12" /><path d="M12 3v18 M10 6h4 M10 10h4 M10 14h4 M10 18h4" />',
    chili: '<path d="M17 4c-3 0-6 3-9 7-2 3-4 7-5 11 0 1 .5 1.5 1.5 1.5 4-1 8-3 11-5 4-3 7-6 7-9 0-3-2.5-5.5-5.5-5.5z" /><path d="M17 4l1.5-1.5" />',
    pumpkin: '<path d="M12 21c-4.42 0-8-3.13-8-7s3.58-7 8-7 8 3.13 8 7-3.58 7-8 7z" /><path d="M12 7c-2 0-4 3-4 7s2 7 4 7 M12 7c2 0 4 3 4 7s-2 7-4 7" /><path d="M12 7V4 M12 4l2-1" />',
    sprout: '<path d="M12 22V10" /><path d="M12 14c-4 0-6-2-6-5s3-4 6-1" /><path d="M12 12c4 0 6-2 6-5s-3-4-6-1" />',
    potato: '<path d="M12 5c4 0 7 2 8 5s0 6-3 8-6 2-9 1-4-3-3-6 3-8 7-8z" /><path d="M9 10h.01 M15 9h.01 M8 14h.01 M13 15h.01 M16 13h.01" stroke-dasharray="0 0" stroke-width="3" stroke-linecap="round" />',
    pot: '<path d="M4 8h16v2H4z" /><path d="M5 10l2 11h10l2-11" />',
    sprinkler: '<path d="M12 22v-6 M8 16h8v-3H8z M10 13l2-3 2 3" /><path d="M6 8A9 9 0 0 1 18 8 M3 11a12 12 0 0 1 18 0 M12 5V2" />',
    pump: '<path d="M18 4H10v4M10 8H6v2h4v8 M10 10h6v3" /><path d="M16 17a2 2 0 0 1-4 0c0-1.5 2-3 2-3s2 1.5 2 3z" />',
    pepper: '<path d="M12 5c-2.5 0-4.5 1.5-4.5 4.5 0 3.5 2 6 3.5 7 1.5.8 1.5 2.5 1 3.5a1 1 0 0 0 1.5 1.2c1.5-1 2-2.7 2-4.2c0-3.5-2-6.5-3.5-7.5" /><path d="M12 5c2.5 0 4.5 1.5 4.5 4.5 0 3.5-2 6-3.5 7" /><path d="M12 5V3c0-.6-.4-1-1-1" />',
    eggplant: '<path d="M18.5 5.5c-2.3-2.3-6.5-.7-8.5 1.3C8 8.8 6.5 12 6.5 15.5c0 3.3 2.7 6 6 6 3.5 0 6.7-1.5 8.7-3.5 2-2 3.6-6.2 1.3-8.5" /><path d="M10 6.8l-4-4" /><path d="M8.5 5.5c.3 1.5 1.2 2.7 2.5 3.3" />',
    broccoli: '<path d="M12 6a3.5 3.5 0 0 0-3.5 3.5c0 .3.05.6.15.9A3.5 3.5 0 0 0 6 13.5a3.5 3.5 0 0 0 3.5 3.5h5a3.5 3.5 0 0 0 3.5-3.5 3.5 3.5 0 0 0-2.65-3.4c.1-.3.15-.6.15-.9A3.5 3.5 0 0 0 12 6z" /><path d="M10 17v4a1 1 0 0 0 1 1h2a1 1 0 0 0 1-1v-4" />',
    pea: '<path d="M3 12c3-4 7-6 11-4s7 5 7 5-3 4-7 4-8-1-11-5z" /><circle cx="8" cy="11" r="2" /><circle cx="12" cy="12" r="2" /><circle cx="16" cy="12" r="2" />',
    radish: '<path d="M12 8c-3 0-5 2-5 5.5C7 17 9.5 21 12 22c2.5-1 5-5 5-8.5c0-3.5-2-5.5-5-5.5z" /><path d="M12 8V2 M9 5c1-1.5 2-3 3-3 M15 5c-1-1.5-2-3-3-3" />',
    cabbage: '<circle cx="12" cy="14" r="7" /><path d="M12 7c-3 0-5 2-5 5 0 2 1.5 3.5 3 4 M12 7c3 0 5 2 5 5 0 2-1.5 3.5-3 4 M9 10a5 5 0 0 1 6 0 M12 7v14" />',
    onion: '<path d="M12 3c-1.5 3-5 5.5-5 9.5a5 5 0 1 0 10 0C17 8.5 13.5 6 12 3z" /><path d="M10 12c.5 2 1.5 4.5 2 5 M14 12c-.5 2-1.5 4.5-2 5 M12 3v14" /><path d="M10 20l2 2 2-2" />',
    garlic: '<path d="M12 2c-.5 2-3 4.5-5 7.5a6 6 0 1 0 10 0c-2-3-4.5-5.5-5-7.5z" /><path d="M12 8c-1 2-2 4-2 7 M12 8c1 2 2 4 2 7 M12 2v15" />',
    mushroom: '<path d="M4 12c0-4.4 3.6-8 8-8s8 3.6 8 8H4z" /><path d="M9 12v7a2 2 0 0 0 2 2h2a2 2 0 0 0 2-2v-7" />',
    leaf: '<path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.48 19 2c1 2 2 4.18 2 8 0 5.5-4.78 10-10 10Z" /><path d="M2 21c0-3 1.85-5.36 5.08-6C9.5 14.52 12 13 13 12" />',
    flower: '<circle cx="12" cy="12" r="3" /><path d="M12 16.5A4.5 4.5 0 1 1 7.5 12 4.5 4.5 0 1 1 12 7.5a4.5 4.5 0 1 1 4.5 4.5 4.5 4.5 0 1 1-4.5 4.5" /><path d="M12 7.5V9 M7.5 12H9 M16.5 12H15 M12 16.5V15" /><path d="m8 8 1.88 1.88 M14.12 9.88 16 8 M8 16 1.88 14.12 M14.12 14.12 16 16" />',
    tree: '<path d="m17 14 3 3.3a1 1 0 0 1-.7 1.7H4.7a1 1 0 0 1-.7-1.7L7 14h-.3a1 1 0 0 1-.7-1.7L9 9h-.2A1 1 0 0 1 8 7.3L12 3l4 4.3a1 1 0 0 1-.8 1.7H15l3 3.3a1 1 0 0 1-.7 1.7H17Z" /><path d="M12 22v-3" />',
    apple: '<path d="M12 20.94c1.5 0 2.75-.75 4-1.94 1.25 1.19 2.5 1.94 4 1.94 1.5 0 3-1.5 3-4 0-4-3.5-5.5-5.5-5.5-1.5 0-2.5.5-3 .5s-1.5-.5-3-.5c-2 0-5.5 1.5-5.5 5.5 0 2.5 1.5 4 3 4 1.5 0 2.75-.75 4-1.94Z" /><path d="M12 2s2 2 2 5.5-2 5.5-2 5.5-2-2-2-5.5 2-5.5 2-5.5z" />',
    banana: '<path d="M4 13c3.5-2 8-2 10 2a5.5 5.5 0 0 1 8 5" /><path d="M5.15 17.89c5.52-1.52 8.65-6.89 7-12C11.55 4 11.5 2 13 2c3.22 0 5 5.5 5 8 0 6.5-4.2 12-10.49 12C5.11 22 2 22 2 20c0-1.5 1.14-1.55 3.15-2.11Z" />',
    cherry: '<path d="M2 17a5 5 0 0 0 10 0c0-2.76-2.5-5-5-3-2.5-2-5 .24-5 3Z" /><path d="M12 17a5 5 0 0 0 10 0c0-2.76-2.5-5-5-3-2.5-2-5 .24-5 3Z" /><path d="M7 14c3.22-2.91 4.29-8.75 5-12 1.66 2.38 4.94 9 5 12" /><path d="M22 9c-4.29 0-7.14-2.33-10-7 5.71 0 10 4.67 10 7Z" />',
    cherries: '<path d="M2 17a5 5 0 0 0 10 0c0-2.76-2.5-5-5-3-2.5-2-5 .24-5 3Z" /><path d="M12 17a5 5 0 0 0 10 0c0-2.76-2.5-5-5-3-2.5-2-5 .24-5 3Z" /><path d="M7 14c3.22-2.91 4.29-8.75 5-12 1.66 2.38 4.94 9 5 12" /><path d="M22 9c-4.29 0-7.14-2.33-10-7 5.71 0 10 4.67 10 7Z" />',
    grape: '<path d="M22 5V2l-5.89 5.89" /><circle cx="16.6" cy="15.89" r="3" /><circle cx="8.11" cy="7.4" r="3" /><circle cx="12.35" cy="11.65" r="3" /><circle cx="13.91" cy="5.85" r="3" /><circle cx="18.15" cy="10.09" r="3" /><circle cx="6.56" cy="13.2" r="3" /><circle cx="10.8" cy="17.44" r="3" /><circle cx="5" cy="19" r="3" />',
    grapes: '<path d="M22 5V2l-5.89 5.89" /><circle cx="16.6" cy="15.89" r="3" /><circle cx="8.11" cy="7.4" r="3" /><circle cx="12.35" cy="11.65" r="3" /><circle cx="13.91" cy="5.85" r="3" /><circle cx="18.15" cy="10.09" r="3" /><circle cx="6.56" cy="13.2" r="3" /><circle cx="10.8" cy="17.44" r="3" /><circle cx="5" cy="19" r="3" />',
    strawberry: '<path d="m17 7 3.5-3.5" /><path d="M17 2v5h5" /><path d="M2.1 17.1a4 4 0 0 0 4.8 4.8l9-2.1a6.32 6.32 0 0 0 2.9-10.9L15 5.2A6.5 6.5 0 0 0 4.1 8.3Z" /><path d="M8.5 9.5h.01 M12.5 8.5h.01 M7.5 13.5h.01 M11.5 12.5h.01 M15.5 11.5h.01 M6.5 17.5h.01 M10.5 16.5h.01 M14.5 15.5h.01" stroke-dasharray="0 0" stroke-width="3" stroke-linecap="round" />',
    pear: '<path d="M22 7a4.95 4.95 0 0 0-8.6-3.4c-1.5 1.6-1.6 1.8-5 2.6a8 8 0 1 0 9.4 9.5c.7-3.4 1-3.6 2.6-5 1-1 1.6-2.3 1.6-3.7" /><path d="m19 5 3-3" />',
    citrus: '<path d="M21.66 17.67a1.08 1.08 0 0 1-.04 1.6A12 12 0 0 1 4.73 2.38a1.1 1.1 0 0 1 1.61-.04z" /><path d="M19.65 15.66A8 8 0 0 1 8.35 4.34" /><path d="m14 10-5.5 5.5" /><path d="M14 17.85V10H6.15" />',
    orange: '<path d="M21.66 17.67a1.08 1.08 0 0 1-.04 1.6A12 12 0 0 1 4.73 2.38a1.1 1.1 0 0 1 1.61-.04z" /><path d="M19.65 15.66A8 8 0 0 1 8.35 4.34" /><path d="m14 10-5.5 5.5" /><path d="M14 17.85V10H6.15" />',
    lemon: '<path d="M21.66 17.67a1.08 1.08 0 0 1-.04 1.6A12 12 0 0 1 4.73 2.38a1.1 1.1 0 0 1 1.61-.04z" /><path d="M19.65 15.66A8 8 0 0 1 8.35 4.34" /><path d="m14 10-5.5 5.5" /><path d="M14 17.85V10H6.15" />',
    pineapple: '<path d="M12 2c1-1 2 .5 2 2 0 1.5-2 3-2 3s-2-1.5-2-3c0-1.5 1-3 2-2z M8 6c0-1.5 1.5-1 1.5 1 0 1-1.5 2-1.5 2s-1-.5-1-1.5 M16 6c0-1.5-1.5-1-1.5 1 0 1 1.5 2 1.5 2s1-.5 1-1.5" /><path d="M12 22c4 0 7-3 7-8 0-4-3-6-7-6s-7 2-7 6c0 5 3 8 7 8z" /><path d="M8 11l8 6 M6 14l6 6 M10 9l6 4 M16 11l-8 6 M18 14l-6 6 M14 9l-6 4" />',
    watermelon: '<path d="M21.7 17.7a1.08 1.08 0 0 1-.08 1.57A12 12 0 0 1 4.73 2.38a1.1 1.1 0 0 1 1.61-.04Z" /><path d="M19.7 15.7A8 8 0 0 1 8.35 4.34" /><path d="M10 11h.01 M13 14h.01" stroke-dasharray="0 0" stroke-width="3" stroke-linecap="round" />',
    melon: '<circle cx="12" cy="12" r="10" /><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 M12 2a15.3 15.3 0 0 0-4 10 15.3 15.3 0 0 0 4 10" />',
    berry: '<circle cx="9" cy="15" r="4" /><circle cx="15" cy="15" r="4" /><circle cx="12" cy="9" r="4" /><path d="M9 11c0-2-1-3-2-3 M15 11c0-2 1-3 2-3 M12 5V2" />',
    berries: '<circle cx="9" cy="15" r="4" /><circle cx="15" cy="15" r="4" /><circle cx="12" cy="9" r="4" /><path d="M9 11c0-2-1-3-2-3 M15 11c0-2 1-3 2-3 M12 5V2" />'
};

class FloraFlowCardSecondary extends HTMLElement {
    constructor() {
        super();
        this.attachShadow({ mode: "open" });
        this.activeRelayId = null; // Tracks which relay is currently open in the dialog
        this.manualWateringStarted = {}; // Tracks manual activation on the client side
    }

    getIconHTML(iconName) {
        const raw = iconName.toLowerCase();
        const svgContent = FLORA_SVGS[raw];
        if (svgContent) {
            return `
                <svg viewBox="0 0 24 24" class="custom-svg-icon">
                    ${svgContent}
                </svg>
            `;
        }

        // Fallback to standard Home Assistant ha-icon
        const resolvedMdi = FLORA_ICONS[raw] || iconName;
        return `<ha-icon icon="${resolvedMdi}"></ha-icon>`;
    }

    isScheduledWateringActive(startT, durationMin) {
        if (!startT || isNaN(durationMin)) return false;

        const now = new Date();
        const currentMinutes = now.getHours() * 60 + now.getMinutes();

        const parts = startT.split(':');
        if (parts.length < 2) return false;
        const startMinutes = parseInt(parts[0]) * 60 + parseInt(parts[1]);

        const endMinutes = startMinutes + durationMin;

        if (endMinutes <= 1440) {
            return currentMinutes >= startMinutes && currentMinutes < endMinutes;
        } else {
            const wrappedEndMinutes = endMinutes - 1440;
            return currentMinutes >= startMinutes || currentMinutes < wrappedEndMinutes;
        }
    }

    setConfig(config) {
        this._config = config;
        this.title = config.title || "FloraFlow Controller";
        this.tempEntity = config.temperature_entity || "sensor.floraflow_temperature";
        this.humidityEntity = config.humidity_entity || "sensor.floraflow_humidity";
        this.columns = config.columns || 2;

        // Default relays 1 to 8 if not defined
        this.relays = config.relays || Array.from({ length: 8 }, (_, i) => ({
            id: i + 1,
            name: `Relay ${i + 1}`,
            icon: "mdi:water-pump"
        }));

        this.renderSkeleton();
    }

    set hass(hass) {
        this._hass = hass;
        this.updateState();
    }

    renderSkeleton() {
        // Build relay box elements
        let relayBoxes = this.relays.map(relay => {
            const id = relay.id;
            const name = relay.name || `Relay ${id}`;
            const rawIcon = relay.icon || "mdi:water-pump";

            const iconColor = relay.icon_color || relay.color || '';
            const customStyles = iconColor ? `
                --custom-icon-color: ${iconColor};
                --custom-bg-color: color-mix(in srgb, ${iconColor} 15%, transparent);
                --custom-inactive-bg-color: color-mix(in srgb, ${iconColor} 8%, transparent);
                --custom-pulse-color: color-mix(in srgb, ${iconColor} 40%, transparent);
            ` : '';

            return `
                <div class="relay-box" id="relay-box-${id}" data-id="${id}" style="${customStyles}">
                    <div class="status-indicator" id="status-indicator-${id}">
                        <span id="status-icon-${id}" class="icon-wrapper">
                            ${this.getIconHTML(rawIcon)}
                        </span>
                    </div>
                    <div class="relay-name">${name}</div>
                    <div class="relay-status" id="status-text-${id}">Loading...</div>
                </div>
            `;
        }).join("");

        this.shadowRoot.innerHTML = `
            <style>
                :host {
                    display: block;
                    font-family: var(--primary-font-family, 'Roboto', sans-serif);
                }
                
                * {
                    box-sizing: border-box;
                }
                
                ha-card {
                    background: var(--ha-card-background, var(--card-background-color, #1e293b));
                    border-radius: var(--ha-card-border-radius, 16px);
                    box-shadow: var(--ha-card-box-shadow, 0 8px 30px rgba(0, 0, 0, 0.3));
                    border: var(--ha-card-border-width, 1px) solid var(--ha-card-border-color, var(--divider-color, rgba(140, 140, 140, 0.15)));
                    padding: 16px;
                    color: var(--primary-text-color, #f8fafc);
                    overflow: hidden;
                    position: relative;
                }

                .card-header {
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    margin-bottom: 16px;
                    padding-bottom: 8px;
                    border-bottom: 1px solid var(--divider-color, rgba(140, 140, 140, 0.15));
                }

                .header-left {
                    display: flex;
                    flex-direction: column;
                    gap: 4px;
                }

                .card-title {
                    font-size: 20px;
                    font-weight: 600;
                    letter-spacing: 0.5px;
                    display: flex;
                    align-items: center;
                    gap: 8px;
                }

                .sensor-values {
                    display: flex;
                    align-items: center;
                    gap: 12px;
                    font-size: 13px;
                    color: var(--secondary-text-color, #cbd5e1);
                }

                .sensor-item {
                    display: flex;
                    align-items: center;
                    gap: 4px;
                }

                .sensor-item ha-icon {
                    --mdc-icon-size: 16px;
                    color: var(--secondary-text-color, #94a3b8);
                }

                .connection-status {
                    display: flex;
                    align-items: center;
                    gap: 6px;
                    font-size: 12px;
                    color: var(--secondary-text-color, #94a3b8);
                    font-weight: 500;
                }

                .status-dot {
                    width: 8px;
                    height: 8px;
                    border-radius: 50%;
                    background-color: #ef4444; /* Default Offline */
                    box-shadow: 0 0 8px #ef4444;
                    transition: all 0.3s ease;
                }

                .status-dot.online {
                    background-color: #10b981;
                    box-shadow: 0 0 8px #10b981;
                }

                /* Grid Layout */
                .relay-grid {
                    display: grid;
                    grid-template-columns: repeat(var(--grid-columns, 2), minmax(0, 1fr));
                    gap: 12px;
                    width: 100%;
                }

                .relay-box {
                    background: var(--secondary-background-color, rgba(140, 140, 140, 0.05));
                    border: 1px solid var(--ha-card-border-color, var(--divider-color, rgba(140, 140, 140, 0.15)));
                    border-radius: 12px;
                    padding: 16px 12px;
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    justify-content: center;
                    text-align: center;
                    cursor: pointer;
                    user-select: none;
                    transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
                    min-width: 0;
                    width: 100%;
                }

                .relay-box:hover {
                    background: var(--secondary-background-color, rgba(140, 140, 140, 0.08));
                    border-color: var(--divider-color, rgba(140, 140, 140, 0.25));
                    transform: translateY(-2px);
                    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.15);
                }

                .relay-box.active {
                    background: var(--custom-bg-color, rgba(14, 165, 233, 0.06));
                    border-color: var(--custom-icon-color, rgba(14, 165, 233, 0.3));
                    box-shadow: 0 4px 20px var(--custom-pulse-color, rgba(14, 165, 233, 0.1));
                }

                .status-indicator {
                    width: 44px;
                    height: 44px;
                    border-radius: 50%;
                    background: var(--custom-inactive-bg-color, var(--secondary-background-color, rgba(140, 140, 140, 0.12)));
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    margin-bottom: 10px;
                    transition: all 0.3s ease;
                    color: var(--custom-icon-color, var(--secondary-text-color, #94a3b8));
                }

                .status-indicator.active {
                    background: var(--custom-bg-color, rgba(14, 165, 233, 0.15));
                    color: var(--custom-icon-color, #0ea5e9);
                    animation: pulse 2.0s infinite ease-in-out;
                }

                @keyframes pulse {
                    0% { transform: scale(1); box-shadow: 0 0 0 0 var(--custom-pulse-color, rgba(14, 165, 233, 0.4)); }
                    70% { transform: scale(1.05); box-shadow: 0 0 0 8px rgba(14, 165, 233, 0); }
                    100% { transform: scale(1); box-shadow: 0 0 0 0 rgba(14, 165, 233, 0); }
                }

                .relay-name {
                    font-size: 14px;
                    font-weight: 600;
                    color: var(--primary-text-color, #f1f5f9);
                    margin-bottom: 4px;
                    white-space: nowrap;
                    overflow: hidden;
                    text-overflow: ellipsis;
                    width: 100%;
                }

                .relay-status {
                    font-size: 11px;
                    color: var(--secondary-text-color, #94a3b8);
                    line-height: 1.2;
                    white-space: nowrap;
                    overflow: hidden;
                    text-overflow: ellipsis;
                    width: 100%;
                }

                .custom-svg-icon {
                    width: 24px;
                    height: 24px;
                    display: inline-block;
                }

                .custom-svg-icon path,
                .custom-svg-icon circle {
                    stroke: currentColor;
                    stroke-width: 2;
                    fill: none;
                    stroke-linecap: round;
                    stroke-linejoin: round;
                }

                .icon-wrapper {
                    display: flex;
                    align-items: center;
                    justify-content: center;
                }

                /* Modal Overlay */
                .modal-overlay {
                    position: fixed;
                    top: 0;
                    left: 0;
                    width: 100vw;
                    height: 100vh;
                    background: rgba(0, 0, 0, 0.75);
                    backdrop-filter: blur(8px);
                    z-index: 10000;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    opacity: 0;
                    pointer-events: none;
                    transition: opacity 0.3s ease;
                }

                .modal-overlay.active {
                    opacity: 1;
                    pointer-events: auto;
                }

                .modal-content {
                    background: var(--ha-card-background, var(--card-background-color, #1e293b));
                    border: 1px solid var(--ha-card-border-color, var(--divider-color, rgba(140, 140, 140, 0.15)));
                    border-radius: 16px;
                    width: 90%;
                    max-width: 380px;
                    padding: 20px;
                    box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.5), 0 10px 10px -5px rgba(0, 0, 0, 0.5);
                    transform: scale(0.9);
                    transition: transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
                    color: var(--primary-text-color, #f8fafc);
                }

                .modal-overlay.active .modal-content {
                    transform: scale(1);
                }

                .modal-header {
                    display: flex;
                    align-items: center;
                    margin-bottom: 16px;
                    padding-bottom: 12px;
                    border-bottom: 1px solid var(--divider-color, rgba(140, 140, 140, 0.15));
                    position: relative;
                }

                .modal-header-icon {
                    width: 36px;
                    height: 36px;
                    border-radius: 50%;
                    background: var(--custom-inactive-bg-color, var(--secondary-background-color, rgba(140, 140, 140, 0.12)));
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    margin-right: 12px;
                    color: var(--custom-icon-color, var(--secondary-text-color, #94a3b8));
                    transition: all 0.3s ease;
                }

                .modal-header-icon.active {
                    background: var(--custom-bg-color, rgba(14, 165, 233, 0.15));
                    color: var(--custom-icon-color, #0ea5e9);
                    animation: modal-pulse 2s infinite ease-in-out;
                }

                @keyframes modal-pulse {
                    0% { transform: scale(1); }
                    50% { transform: scale(1.05); }
                    100% { transform: scale(1); }
                }

                .modal-title {
                    font-size: 18px;
                    font-weight: 600;
                    flex: 1;
                }

                #modal-close-btn {
                    color: var(--secondary-text-color, #94a3b8);
                    cursor: pointer;
                    transition: color 0.2s;
                    margin-right: -8px;
                }

                #modal-close-btn:hover {
                    color: var(--primary-text-color, #f1f5f9);
                }

                .modal-body {
                    display: flex;
                    flex-direction: column;
                    gap: 4px;
                }

                .control-row {
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    padding: 12px 0;
                }

                .control-row:not(:last-child) {
                    border-bottom: 1px solid var(--divider-color, rgba(140, 140, 140, 0.08));
                }

                .control-label {
                    font-size: 14px;
                    color: var(--primary-text-color, #cbd5e1);
                    font-weight: 550;
                }

                .time-input {
                    background: var(--secondary-background-color, rgba(140, 140, 140, 0.05));
                    border: 1px solid var(--divider-color, rgba(140, 140, 140, 0.15));
                    border-radius: 6px;
                    color: var(--primary-text-color, #f1f5f9);
                    font-family: inherit;
                    font-size: 13px;
                    padding: 4px 8px;
                    outline: none;
                    text-align: center;
                }

                .time-input:focus {
                    border-color: var(--primary-color, #0ea5e9);
                    background: var(--secondary-background-color, rgba(140, 140, 140, 0.08));
                }

                .time-input:disabled {
                    opacity: 0.5;
                    cursor: not-allowed;
                }

                .slider-container {
                    display: flex;
                    align-items: center;
                    gap: 12px;
                    flex: 1;
                    justify-content: flex-end;
                    max-width: 60%;
                }

                .duration-slider {
                    -webkit-appearance: none;
                    width: 100%;
                    height: 4px;
                    border-radius: 2px;
                    background: var(--secondary-background-color, rgba(140, 140, 140, 0.15));
                    outline: none;
                    transition: all 0.3s;
                }

                .duration-slider::-webkit-slider-thumb {
                    -webkit-appearance: none;
                    appearance: none;
                    width: 14px;
                    height: 14px;
                    border-radius: 50%;
                    background: var(--primary-color, #0ea5e9);
                    cursor: pointer;
                    box-shadow: 0 0 6px var(--primary-color, rgba(14, 165, 233, 0.5));
                    transition: all 0.2s;
                }

                .duration-slider::-webkit-slider-thumb:hover {
                    transform: scale(1.2);
                }

                .slider-value {
                    font-size: 13px;
                    font-weight: 500;
                    color: var(--primary-text-color, #f1f5f9);
                    min-width: 48px;
                    text-align: right;
                }

                ha-switch {
                    --switch-checked-button-color: var(--primary-color, #0ea5e9);
                    --switch-checked-track-color: rgba(14, 165, 233, 0.5);
                }
            </style>

            <ha-card>
                <div class="card-header">
                    <div class="header-left">
                        <div class="card-title">
                            <ha-icon icon="mdi:sprinkler-variant"></ha-icon>
                            <span>${this.title}</span>
                        </div>
                        <div class="sensor-values" id="sensor-values" style="display: none;">
                            <span class="sensor-item">
                                <ha-icon icon="mdi:thermometer"></ha-icon>
                                <span id="temp-value">--</span>°C
                            </span>
                            <span class="sensor-item">
                                <ha-icon icon="mdi:water-percent"></ha-icon>
                                <span id="humidity-value">--</span>%
                            </span>
                        </div>
                    </div>
                    <div class="connection-status" id="connection-status">
                        <div class="status-dot" id="status-dot"></div>
                        <span id="connection-text">Offline</span>
                    </div>
                </div>
                
                <div class="relay-grid" style="--grid-columns: ${this.columns};">
                    ${relayBoxes}
                </div>

                <!-- Modal Dialog Config -->
                <div class="modal-overlay" id="config-modal">
                    <div class="modal-content">
                        <div class="modal-header">
                            <div class="modal-header-icon" id="modal-icon-container">
                                <ha-icon id="modal-icon" icon="mdi:water-pump"></ha-icon>
                            </div>
                            <span class="modal-title" id="modal-title">Configure Relay</span>
                            <ha-icon-button id="modal-close-btn" icon="mdi:close">
                                <ha-icon icon="mdi:close"></ha-icon>
                            </ha-icon-button>
                        </div>
                        
                        <div class="modal-body">
                            <div class="control-row">
                                <span class="control-label">Manual Watering</span>
                                <ha-switch id="modal-manual-switch"></ha-switch>
                            </div>
                            
                            <div class="control-row">
                                <span class="control-label">Automatic Schedule</span>
                                <ha-switch id="modal-schedule-switch"></ha-switch>
                            </div>
                            
                            <div class="control-row" style="flex-direction: column; align-items: stretch; gap: 8px; border-bottom: none;">
                                <div style="display: flex; justify-content: space-between; align-items: center;">
                                    <span class="control-label">Start Times</span>
                                    <ha-icon-button id="modal-add-time-btn" icon="mdi:plus" style="color: var(--primary-color, #0ea5e9); --mdc-icon-button-size: 32px;">
                                        <ha-icon icon="mdi:plus"></ha-icon>
                                    </ha-icon-button>
                                </div>
                                <div id="start-times-container" style="display: flex; flex-direction: column; gap: 8px;">
                                    <!-- Dynamic rows inserted here -->
                                </div>
                            </div>
                            
                            <div class="control-row">
                                <span class="control-label">Duration</span>
                                <div class="slider-container">
                                    <input type="range" min="1" max="10" value="1" class="duration-slider" id="modal-duration-slider">
                                    <span class="slider-value" id="modal-duration-value">1 min</span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </ha-card>
        `;

        // Register event listeners for each grid tile box
        this.relays.forEach(relay => {
            const id = relay.id;
            const box = this.shadowRoot.getElementById(`relay-box-${id}`);
            if (box) {
                box.addEventListener('click', () => this.openDialog(id));
            }
        });

        // Register modal closing events
        const closeBtn = this.shadowRoot.getElementById('modal-close-btn');
        if (closeBtn) {
            closeBtn.addEventListener('click', () => this.closeDialog());
        }

        const modalOverlay = this.shadowRoot.getElementById('config-modal');
        if (modalOverlay) {
            modalOverlay.addEventListener('click', (e) => {
                if (e.target === modalOverlay) {
                    this.closeDialog();
                }
            });
        }

        // Register action event listeners for modal controls
        const manualSwitch = this.shadowRoot.getElementById('modal-manual-switch');
        if (manualSwitch) {
            manualSwitch.addEventListener('change', (e) => {
                if (this.activeRelayId !== null) {
                    this.handleManualSwitch(this.activeRelayId, e);
                }
            });
        }

        const scheduleSwitch = this.shadowRoot.getElementById('modal-schedule-switch');
        if (scheduleSwitch) {
            scheduleSwitch.addEventListener('change', (e) => {
                if (this.activeRelayId !== null) {
                    this.handleScheduleSwitch(this.activeRelayId, e);
                }
            });
        }

        const addTimeBtn = this.shadowRoot.getElementById('modal-add-time-btn');
        if (addTimeBtn) {
            addTimeBtn.addEventListener('click', () => {
                if (this.activeRelayId !== null) {
                    if (!this._tempStartTimes) {
                        this._tempStartTimes = [{"time": "12:00:00", "enabled": true}];
                    } else {
                        this._tempStartTimes.push({ "time": "12:00:00", "enabled": true });
                    }
                    this.renderStartTimesList(this.activeRelayId, this._tempStartTimes);
                    this.saveStartTimes(this.activeRelayId);
                }
            });
        }

        const durationSlider = this.shadowRoot.getElementById('modal-duration-slider');
        const durationValue = this.shadowRoot.getElementById('modal-duration-value');
        if (durationSlider) {
            durationSlider.addEventListener('input', (e) => {
                if (durationValue) {
                    durationValue.textContent = `${e.target.value} min`;
                }
            });
            durationSlider.addEventListener('change', (e) => {
                if (this.activeRelayId !== null) {
                    this.handleDurationChange(this.activeRelayId, e);
                }
            });
        }
    }

    openDialog(id) {
        this.activeRelayId = id;

        // Find configuration info
        const relay = this.relays.find(r => r.id === id);
        if (!relay) return;

        // Set title and icon of the modal header
        const modalTitle = this.shadowRoot.getElementById('modal-title');
        const modalIconContainer = this.shadowRoot.getElementById('modal-icon-container');
        const modalContent = this.shadowRoot.querySelector('.modal-content');

        if (modalTitle) modalTitle.textContent = relay.name || `Relay ${id}`;

        const rawIcon = relay.icon || "mdi:water-pump";
        if (modalIconContainer) {
            modalIconContainer.innerHTML = this.getIconHTML(rawIcon);
        }

        // Apply custom colors to modal content styling if specified
        if (modalContent) {
            const iconColor = relay.icon_color || relay.color || '';
            if (iconColor) {
                modalContent.style.setProperty('--custom-icon-color', iconColor);
                modalContent.style.setProperty('--custom-bg-color', `color-mix(in srgb, ${iconColor} 15%, transparent)`);
                modalContent.style.setProperty('--custom-inactive-bg-color', `color-mix(in srgb, ${iconColor} 8%, transparent)`);
                modalContent.style.setProperty('--custom-pulse-color', `color-mix(in srgb, ${iconColor} 40%, transparent)`);
            } else {
                modalContent.style.removeProperty('--custom-icon-color');
                modalContent.style.removeProperty('--custom-bg-color');
                modalContent.style.removeProperty('--custom-inactive-bg-color');
                modalContent.style.removeProperty('--custom-pulse-color');
            }
        }

        // Show dialog
        const modal = this.shadowRoot.getElementById('config-modal');
        if (modal) {
            modal.classList.add('active');
        }

        // Fetch current start times from HA state and render
        const startTimesEnt = this.getEntityName(id, 'start_times_entity', `sensor.floraflow_relay_${id}_start_times`);
        const startTimesStateObj = this._hass.states[startTimesEnt];
        let startTimes = [{ "time": "08:00:00", "enabled": true }];
        if (startTimesStateObj && startTimesStateObj.state && startTimesStateObj.state !== 'unknown' && startTimesStateObj.state !== 'unavailable') {
            try {
                startTimes = JSON.parse(startTimesStateObj.state);
            } catch (e) {
                console.error("Error parsing start times state", e);
            }
        }
        this.renderStartTimesList(id, startTimes);

        // Immediately update status and input values in the dialog
        this.updateState();
    }

    closeDialog() {
        const modal = this.shadowRoot.getElementById('config-modal');
        if (modal) {
            modal.classList.remove('active');
        }
        this.activeRelayId = null;
    }

    handleManualSwitch(id, event) {
        const entity = this.getEntityName(id, 'relay_entity', `switch.floraflow_relay_${id}`);
        const service = event.target.checked ? 'turn_on' : 'turn_off';

        if (!this.manualWateringStarted) {
            this.manualWateringStarted = {};
        }
        this.manualWateringStarted[id] = event.target.checked;

        this._hass.callService('switch', service, { entity_id: entity });
    }

    handleScheduleSwitch(id, event) {
        const entity = this.getEntityName(id, 'schedule_enabled_entity', `switch.floraflow_relay_${id}_schedule_enabled`);
        const service = event.target.checked ? 'turn_on' : 'turn_off';
        this._hass.callService('switch', service, { entity_id: entity });
    }

    renderStartTimesList(id, startTimes) {
        const container = this.shadowRoot.getElementById('start-times-container');
        if (!container) return;

        this._tempStartTimes = JSON.parse(JSON.stringify(startTimes));

        container.innerHTML = this._tempStartTimes.map((item, index) => {
            const timeVal = item.time.substring(0, 5); // Format HH:MM
            return `
                <div class="control-row" style="padding: 4px 0; border-bottom: none;" data-index="${index}">
                    <div style="display: flex; align-items: center; gap: 8px;">
                        <ha-switch class="time-enabled-switch"></ha-switch>
                        <span class="control-label" style="font-size: 13px;">Time ${index + 1}</span>
                    </div>
                    <div style="display: flex; align-items: center; gap: 8px;">
                        <input type="time" class="time-input list-time-input" value="${timeVal}" step="60">
                        <ha-icon-button class="time-delete-btn" icon="mdi:delete" style="color: #ef4444; --mdc-icon-button-size: 32px;">
                            <ha-icon icon="mdi:delete"></ha-icon>
                        </ha-icon-button>
                    </div>
                </div>
            `;
        }).join("");

        // Register dynamic event listeners and set initial properties
        const rows = container.querySelectorAll('.control-row');
        rows.forEach((row) => {
            const index = parseInt(row.getAttribute('data-index'));
            const item = this._tempStartTimes[index];
            
            const switchEl = row.querySelector('.time-enabled-switch');
            if (switchEl) {
                switchEl.checked = item.enabled;
                switchEl.addEventListener('change', (e) => {
                    this._tempStartTimes[index].enabled = e.target.checked;
                    const timeInput = row.querySelector('.list-time-input');
                    if (timeInput) timeInput.disabled = !e.target.checked;
                    this.saveStartTimes(id);
                });
            }

            const inputEl = row.querySelector('.list-time-input');
            if (inputEl) {
                inputEl.disabled = !item.enabled;
                inputEl.addEventListener('change', (e) => {
                    let val = e.target.value;
                    if (val && val.split(':').length === 2) {
                        val = `${val}:00`;
                    }
                    this._tempStartTimes[index].time = val;
                    this.saveStartTimes(id);
                });
            }

            const deleteBtn = row.querySelector('.time-delete-btn');
            if (deleteBtn) {
                const isOnlyOne = this._tempStartTimes.length === 1;
                deleteBtn.disabled = isOnlyOne;
                if (!isOnlyOne) {
                    deleteBtn.addEventListener('click', () => {
                        this._tempStartTimes.splice(index, 1);
                        this.renderStartTimesList(id, this._tempStartTimes);
                        this.saveStartTimes(id);
                    });
                }
            }
        });
    }

    saveStartTimes(id) {
        const payload = JSON.stringify(this._tempStartTimes);
        this._hass.callService('mqtt', 'publish', {
            topic: `garden/relay/${id}/start_times/set`,
            payload: payload
        });
    }

    getNextStartTime(startTimes) {
        const activeTimes = startTimes.filter(item => item.enabled);
        if (activeTimes.length === 0) return null;

        const now = new Date();
        const currentMin = now.getHours() * 60 + now.getMinutes();

        const parseToMin = (tStr) => {
            const parts = tStr.split(':');
            return parseInt(parts[0]) * 60 + parseInt(parts[1]);
        };

        let nextTime = null;
        let minDiff = 2880;

        activeTimes.forEach(item => {
            const min = parseToMin(item.time);
            const diff = (min - currentMin + 1440) % 1440;
            if (diff < minDiff) {
                minDiff = diff;
                nextTime = item.time.substring(0, 5);
            }
        });

        return nextTime;
    }

    handleDurationChange(id, event) {
        const entity = this.getEntityName(id, 'duration_entity', `number.floraflow_relay_${id}_duration`);
        const value = parseInt(event.target.value);
        this._hass.callService('number', 'set_value', {
            entity_id: entity,
            value: value
        });
    }

    getEntityName(id, configKey, defaultVal) {
        const rConf = this.relays.find(r => r.id === id);
        return (rConf && rConf[configKey]) ? rConf[configKey] : defaultVal;
    }

    updateState() {
        if (!this._hass) return;

        let systemOnline = false;

        this.relays.forEach(relay => {
            const id = relay.id;

            // Resolve actual entity IDs
            const relayEnt = this.getEntityName(id, 'relay_entity', `switch.floraflow_relay_${id}`);
            const schedEnt = this.getEntityName(id, 'schedule_enabled_entity', `switch.floraflow_relay_${id}_schedule_enabled`);
            const startTimesEnt = this.getEntityName(id, 'start_times_entity', `sensor.floraflow_relay_${id}_start_times`);
            const durEnt = this.getEntityName(id, 'duration_entity', `number.floraflow_relay_${id}_duration`);

            // Read states from HA db
            const relayStateObj = this._hass.states[relayEnt];
            const schedStateObj = this._hass.states[schedEnt];
            const startTimesStateObj = this._hass.states[startTimesEnt];
            const durStateObj = this._hass.states[durEnt];

            // If at least one entity is available and not in "unavailable" state, consider system online
            if (relayStateObj && relayStateObj.state !== 'unavailable') {
                systemOnline = true;
            }

            const isOn = relayStateObj ? (relayStateObj.state === 'on') : false;
            const schedEnabled = schedStateObj ? (schedStateObj.state === 'on') : false;

            if (!this.manualWateringStarted) {
                this.manualWateringStarted = {};
            }
            if (!isOn) {
                this.manualWateringStarted[id] = false;
            }

            // Parse start times list
            let startTimes = [{ "time": "08:00:00", "enabled": true }];
            if (startTimesStateObj && startTimesStateObj.state && startTimesStateObj.state !== 'unknown' && startTimesStateObj.state !== 'unavailable') {
                try {
                    startTimes = JSON.parse(startTimesStateObj.state);
                } catch (e) {
                    console.error("Error parsing start times state", e);
                }
            }

            // Read duration
            const durVal = durStateObj ? parseInt(durStateObj.state) : 10;

            // 1. Update Grid Box and Status Indicator CSS
            const box = this.shadowRoot.getElementById(`relay-box-${id}`);
            const indicator = this.shadowRoot.getElementById(`status-indicator-${id}`);
            if (box) {
                if (isOn) {
                    box.classList.add('active');
                } else {
                    box.classList.remove('active');
                }
            }
            if (indicator) {
                if (isOn) {
                    indicator.classList.add('active');
                } else {
                    indicator.classList.remove('active');
                }
            }

            // 2. Update Box Status Text
            const statusLabel = this.shadowRoot.getElementById(`status-text-${id}`);
            if (statusLabel) {
                if (isOn) {
                    const isScheduledActive = schedEnabled && !this.manualWateringStarted[id] &&
                        startTimes.some(item => item.enabled && this.isScheduledWateringActive(item.time.substring(0, 5), durVal));
                    if (isScheduledActive) {
                        statusLabel.textContent = `Watering (${durVal} m)`;
                    } else {
                        statusLabel.textContent = "Watering";
                    }
                    statusLabel.style.color = '#38bdf8'; // Sky blue
                } else if (schedEnabled) {
                    const nextTime = this.getNextStartTime(startTimes);
                    if (nextTime) {
                        statusLabel.textContent = `At ${nextTime}`;
                        statusLabel.style.color = '#34d399'; // Mint green
                    } else {
                        statusLabel.textContent = "No Schedule Time";
                        statusLabel.style.color = '#cbd5e1';
                    }
                } else {
                    statusLabel.textContent = "Manual";
                    statusLabel.style.color = '#94a3b8'; // Slate grey
                }
            }

            // 3. Update Modal Dialog controls if this relay is currently active in the modal
            if (this.activeRelayId === id) {
                const manualSwitch = this.shadowRoot.getElementById('modal-manual-switch');
                if (manualSwitch && document.activeElement !== manualSwitch) {
                    manualSwitch.checked = isOn;
                    manualSwitch.disabled = !relayStateObj || relayStateObj.state === 'unavailable';
                }

                const schedSwitch = this.shadowRoot.getElementById('modal-schedule-switch');
                if (schedSwitch && document.activeElement !== schedSwitch) {
                    schedSwitch.checked = schedEnabled;
                    schedSwitch.disabled = !schedStateObj || schedStateObj.state === 'unavailable';
                }

                // Start times list is rendered once when the modal is opened, or updated locally on actions.
                // We do not overwrite it here to avoid race conditions with HA states.

                const durationSlider = this.shadowRoot.getElementById('modal-duration-slider');
                const durationValue = this.shadowRoot.getElementById('modal-duration-value');
                if (durationSlider && document.activeElement !== durationSlider && !isNaN(durVal)) {
                    durationSlider.value = durVal;
                    if (durationValue) {
                        durationValue.textContent = `${durVal} min`;
                    }
                    durationSlider.disabled = !durStateObj || durStateObj.state === 'unavailable';
                }

                const modalIconContainer = this.shadowRoot.getElementById('modal-icon-container');
                if (modalIconContainer) {
                    if (isOn) {
                        modalIconContainer.classList.add('active');
                    } else {
                        modalIconContainer.classList.remove('active');
                    }
                }
            }
        });

        // Update Overall Card Status Dot
        const statusDot = this.shadowRoot.getElementById('status-dot');
        const statusText = this.shadowRoot.getElementById('connection-text');
        if (statusDot && statusText) {
            if (systemOnline) {
                statusDot.classList.add('online');
                statusText.textContent = "Online";
                statusText.style.color = "#10b981";
            } else {
                statusDot.classList.remove('online');
                statusText.textContent = "Offline";
                statusText.style.color = "#ef4444";
            }
        }

        // Update temperature and humidity display
        const tempStateObj = this._hass.states[this.tempEntity];
        const humidityStateObj = this._hass.states[this.humidityEntity];
        const tempElement = this.shadowRoot.getElementById('temp-value');
        const humidityElement = this.shadowRoot.getElementById('humidity-value');
        const sensorContainer = this.shadowRoot.getElementById('sensor-values');

        if (sensorContainer) {
            if (systemOnline && tempStateObj && humidityStateObj &&
                tempStateObj.state !== 'unavailable' && tempStateObj.state !== 'unknown' &&
                humidityStateObj.state !== 'unavailable' && humidityStateObj.state !== 'unknown') {

                sensorContainer.style.display = 'flex';
                if (tempElement) tempElement.textContent = tempStateObj.state;
                if (humidityElement) humidityElement.textContent = humidityStateObj.state;
            } else {
                sensorContainer.style.display = 'none';
            }
        }
    }

    getCardSize() {
        return Math.ceil(this.relays.length / this.columns) * 1.5 + 1;
    }
}

customElements.define("floraflow-card-secondary", FloraFlowCardSecondary);
customElements.define("floraflow-card", class extends FloraFlowCardSecondary {});

// Add preview information in Home Assistant custom card selector
window.customCards = window.customCards || [];
window.customCards.push({
    type: "floraflow-card-secondary",
    name: "FloraFlow Irrigation Card (Grid Layout)",
    description: "A premium grid-based dashboard card to control scheduled and manual irrigation valves with configuration dialogs.",
    preview: false,
});
window.customCards.push({
    type: "floraflow-card",
    name: "FloraFlow Irrigation Card (Grid Layout) Alias",
    description: "Alias for FloraFlow Irrigation Card.",
    preview: false,
});
