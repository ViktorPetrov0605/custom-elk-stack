#!/usr/bin/env node
/**
 * Kibana Dashboard Fix Script
 * Removes visualization that uses non-existent network.type field
 */

const fs = require('fs');

// Fix Conversations Dashboard - Remove IP Version panel
const convDash = JSON.parse(fs.readFileSync('/tmp/dash-conv.json', 'utf8'));
const panels = JSON.parse(convDash.dashboard.panelsJSON);

console.log('Original panels:');
panels.forEach(p => console.log(` - ${p.title}`));

// Find and remove panels that use network.type
const fixedPanels = panels.filter(panel => {
  const config = panel.embeddableConfig?.attributes?.state?.datasourceStates?.formBased?.layers;
  if (!config) return true;
  
  for (const layerId of Object.keys(config)) {
    const layer = config[layerId];
    const columns = layer?.columns || {};
    for (const colId of Object.keys(columns)) {
      const col = columns[colId];
      if (col.sourceField === 'network.type') {
        console.log(`\nREMOVING panel "${panel.title}" - uses non-existent field network.type`);
        return false;
      }
    }
  }
  return true;
});

console.log('\nFixed panels:');
fixedPanels.forEach(p => console.log(` - ${p.title}`));

// Update the dashboard
convDash.dashboard.panelsJSON = JSON.stringify(fixedPanels);

// Save fixed dashboard
fs.writeFileSync('/tmp/dash-conv-fixed.json', JSON.stringify(convDash, null, 2));
console.log('\nSaved: /tmp/dash-conv-fixed.json');

// Also save the panels count change
console.log(`Panel count: ${panels.length} -> ${fixedPanels.length}`);
