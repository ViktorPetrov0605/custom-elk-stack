#!/usr/bin/env node
// Script to fix Kibana dashboards by removing problematic panels

const fs = require('fs');

// Read the exported file
const data = fs.readFileSync('/tmp/all-dash.ndjson', 'utf8');
const lines = data.trim().split('\n');

let fixedLines = [];
let removedPanels = [];

for (const line of lines) {
    if (!line.trim()) continue;
    
    const obj = JSON.parse(line);
    
    if (obj.type === 'dashboard' && obj.attributes && obj.attributes.panelsJSON) {
        const panels = JSON.parse(obj.attributes.panelsJSON);
        const originalPanelCount = panels.length;
        
        // Filter out problematic panels
        const fixedPanels = panels.filter(panel => {
            const panelStr = JSON.stringify(panel);
            
            // Check for network.type (doesn't exist)
            if (panelStr.includes('network.type')) {
                removedPanels.push({
                    dashboard: obj.attributes.title,
                    panelIndex: panel.panelIndex,
                    title: panel.title,
                    reason: 'Uses network.type (field does not exist)'
                });
                return false;
            }
            
            // Check for AS number fields (no data)
            if (panelStr.includes('source.as.number') || panelStr.includes('destination.as.number')) {
                removedPanels.push({
                    dashboard: obj.attributes.title,
                    panelIndex: panel.panelIndex,
                    title: panel.title,
                    reason: 'Uses source.as.number or destination.as.number (no data available)'
                });
                return false;
            }
            
            return true;
        });
        
        obj.attributes.panelsJSON = JSON.stringify(fixedPanels);
        console.log(`${obj.attributes.title}: ${originalPanelCount} panels -> ${fixedPanels.length} panels`);
    }
    
    fixedLines.push(JSON.stringify(obj));
}

// Write fixed dashboards
fs.writeFileSync('/tmp/fixed-dash.ndjson', fixedLines.join('\n') + '\n');

// Report to stderr AND stdout
console.log('\n=== Removed Panels ===');
removedPanels.forEach(panel => {
    console.log(`- ${panel.title} from "${panel.dashboard}" (${panel.reason})`);
});
console.log(`\nTotal removed: ${removedPanels.length} panels`);
