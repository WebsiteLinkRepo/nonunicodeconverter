const NATIVE_HOST_NAME = 'com.nonunicodeconverter.rtf_clipboard_poc';

const pingButton = document.getElementById('pingButton');
const testButton = document.getElementById('testButton');
const statusDiv = document.getElementById('status');

function showStatus(message, type = 'info') {
  statusDiv.textContent = message;
  statusDiv.className = type;
}

// Ping button handler - tests basic connectivity
pingButton.addEventListener('click', async () => {
  pingButton.disabled = true;
  showStatus('Testing connection to native host...', 'info');

  try {
    const port = chrome.runtime.connectNative(NATIVE_HOST_NAME);
    let responseReceived = false;

    port.onMessage.addListener((response) => {
      responseReceived = true;
      console.log('Ping response:', response);

      if (response.success) {
        showStatus(
          '✓ Connection works! Native host responded to ping.\n\n' +
          'The Native Messaging bridge is functional.\n' +
          'Check C:\\rtf_native_debug.log for details.',
          'success'
        );
      } else {
        showStatus(
          `Ping failed: ${response.error || 'Unknown error'}\n\n` +
          `Check C:\\rtf_native_debug.log for details.`,
          'error'
        );
      }

      port.disconnect();
      pingButton.disabled = false;
    });

    port.onDisconnect.addListener(() => {
      if (!responseReceived) {
        const error = chrome.runtime.lastError;
        showStatus(
          `Connection failed.\n\n` +
          `Error: ${error ? error.message : 'Unknown'}\n\n` +
          `Possible causes:\n` +
          `• Extension ID not updated in manifest\n` +
          `• Native host not installed\n` +
          `• Chrome not restarted\n\n` +
          `Check C:\\rtf_native_debug.log for details.`,
          'error'
        );
      }
      pingButton.disabled = false;
    });

    // Send ping message
    port.postMessage({ action: 'ping' });

    // Timeout after 5 seconds
    setTimeout(() => {
      if (!responseReceived) {
        showStatus(
          'Timeout: No response from native host.\n\n' +
          'Check C:\\rtf_native_debug.log for details.',
          'error'
        );
        port.disconnect();
        pingButton.disabled = false;
      }
    }, 5000);

  } catch (error) {
    showStatus(`Exception: ${error.message}`, 'error');
    pingButton.disabled = false;
  }
});

testButton.addEventListener('click', async () => {
  testButton.disabled = true;
  showStatus('Connecting to native host...', 'info');

  try {
    const port = chrome.runtime.connectNative(NATIVE_HOST_NAME);

    let responseReceived = false;

    port.onMessage.addListener((response) => {
      responseReceived = true;
      console.log('Received from native host:', response);

      if (response.success) {
        showStatus(
          'SUCCESS! Native RTF written to clipboard.\n\n' +
          'The Windows clipboard now contains:\n' +
          '• Rich Text Format (registered format)\n' +
          '• CF_UNICODETEXT (plain text)\n' +
          '• HTML Format\n\n' +
          'Now test in PageMaker 7.0!',
          'success'
        );
      } else {
        showStatus(`Error: ${response.error || 'Unknown error'}`, 'error');
      }

      port.disconnect();
      testButton.disabled = false;
    });

    port.onDisconnect.addListener(() => {
      if (!responseReceived) {
        const error = chrome.runtime.lastError;
        showStatus(
          `Native host disconnected.\n\n` +
          `Error: ${error ? error.message : 'Unknown'}\n\n` +
          `Make sure the native host is installed and registered.\n` +
          `Check C:\\rtf_native_debug.log for details.`,
          'error'
        );
      }
      testButton.disabled = false;
    });

    // Send test RTF payload
    const message = {
      action: 'set_clipboard',
      plain_text: 'TEST',
      rtf_text: '{\\rtf1\\ansi{\\fonttbl{\\f0 Arial;}}\\f0 TEST}',
      html_text: '<html><body><p style="font-family: Arial">TEST</p></body></html>'
    };

    port.postMessage(message);

    // Timeout after 5 seconds
    setTimeout(() => {
      if (!responseReceived) {
        showStatus(
          'Timeout: No response from native host.\n\n' +
          'Check C:\\rtf_native_debug.log for details.',
          'error'
        );
        port.disconnect();
        testButton.disabled = false;
      }
    }, 5000);

  } catch (error) {
    showStatus(`Exception: ${error.message}`, 'error');
    testButton.disabled = false;
  }
});
