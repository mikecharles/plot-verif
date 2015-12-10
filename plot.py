#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator
import numpy as np
import warnings


warnings.simplefilter(action="ignore", category=FutureWarning)

pd.set_option('display.mpl_style', 'default')

# colors = [
#     [0, 0, 0],
#     [0.89411765, 0.10196078, 0.10980392],
#     [0.89411765, 0.10196078, 0.10980392],
#     [0.21568627, 0.49411765, 0.72156863],
#     [0.21568627, 0.49411765, 0.72156863],
#     [0.30196078, 0.68627451, 0.29019608],
#     [0.30196078, 0.68627451, 0.29019608],
# ]
# linestyles = [
#     '-',
#     '-',
#     '--',
#     '-',
#     '--',
#     '-',
#     '--',
# ]
# colors = [
#     [0, 0, 0],
#     [0.89411765, 0.10196078, 0.10980392],
#     [0.89411765, 0.10196078, 0.10980392],
#     [0.21568627, 0.49411765, 0.72156863],
#     [0.21568627, 0.49411765, 0.72156863],
# ]
# linestyles = [
#     '-',
#     '-',
#     '--',
#     '-',
#     '--',
# ]
# colors = [
#     [0.89411765, 0.10196078, 0.10980392],
#     [0.89411765, 0.10196078, 0.10980392],
#     [0.21568627, 0.49411765, 0.72156863],
#     [0.21568627, 0.49411765, 0.72156863],
# ]
# linestyles = [
#     '-',
#     '--',
#     '-',
#     '--',
# ]
# colors = [
#     [0.89411765, 0.10196078, 0.10980392],
#     [0.21568627, 0.49411765, 0.72156863],
#     [0.30196078, 0.68627451, 0.29019608],
#     [0.2, 0.2, 0.2],
# ]
# linestyles = [
#     '-',
#     '-',
#     '-',
#     '-',
# ]
colors = [
    [0.89411765, 0.10196078, 0.10980392],
    [1.00000000, 0.49803922, 0.00000000],
    [0.30196078, 0.68627451, 0.29019608],
    [0.96862745, 0.50588235, 0.74901961],
    [0.21568627, 0.49411765, 0.72156863],
]
colors = [
    [0.89411765, 0.10196078, 0.10980392],
    [0.21568627, 0.49411765, 0.72156863],
]
linestyles = [
    '-',
    '-',
]
ncol = 3
dpi = 600

# ------------------------------------------------------------------------------
# Plot heidke
#
print('\nHeidke\n------')
# Load CSV
data = pd.read_csv('heidke_stn.csv',
                   parse_dates=['Date'], index_col='Date',
                   skip_blank_lines=True)
# Create empty figure
fig = plt.figure(figsize=(8, 4))
# Plot data
for i, column in enumerate(data):
    ax = data[column].plot(ax=fig.gca(), color=colors[i],
                           linestyle=linestyles[i], linewidth=0.9)
# Set ylim/ticks
ylim = (-40, 70)
ax.set_ylim(ylim)
plt.tick_params(which='major', length=7)
plt.tick_params(which='minor', length=4, color='k')
ax.yaxis.set_minor_locator(FixedLocator(np.arange(ylim[0], ylim[1] + 1, 2.0)))
ax.yaxis.set_major_locator(FixedLocator(np.arange(ylim[0], ylim[1] + 1, 10)))
# Set legend properties
legend = ax.legend(ncol=ncol, columnspacing=0.7, borderaxespad=0)
legend.draw_frame(False)
plt.setp(legend.get_texts(), fontsize='small')
# Draw labels
plt.title('Heidke Skill Score')
plt.xlabel('Valid Date')
plt.ylabel('Score')
# Plot zero-line
plt.axhline(0, 0, data.shape[1], color='k', linestyle='dashed', zorder=0)
# Plot averages of all series
for i, column in enumerate(data):
    plt.axhline(data[column].mean(), 0, xmax=(1 + 15/len(data)),
                color=colors[i], linestyle='-', linewidth=0.7, clip_on=False)
# Save figure
fig.savefig('heidke_stn.png', dpi=dpi, bbox_inches='tight')
# Display means
print(data.mean())

# ------------------------------------------------------------------------------
# Plot rpss
#
print('\nRPSS\n----')
# Load CSV
data = pd.read_csv('rpss_stn.csv',
                   parse_dates=['Date'], index_col='Date',
                   skip_blank_lines=True)
# Create empty figure
fig = plt.figure(figsize=(8, 4))
# Plot data
for i, column in enumerate(data):
    ax = data[column].plot(ax=fig.gca(), color=colors[i],
                           linestyle=linestyles[i], linewidth=1)
# Set ylim
ylim = (-0.6, 0.6)
ax.set_ylim(ylim)
plt.tick_params(which='major', length=7)
plt.tick_params(which='minor', length=4, color='k')
ax.yaxis.set_minor_locator(FixedLocator(np.arange(ylim[0], ylim[1] + 1, 0.02)))
ax.yaxis.set_major_locator(FixedLocator(np.arange(ylim[0], ylim[1] + 1, 0.1)))
# Set legend properties
legend = ax.legend(ncol=ncol, columnspacing=0.7, borderaxespad=0)
legend.draw_frame(False)
plt.setp(legend.get_texts(), fontsize='small')
# Draw labels
plt.title('RPSS')
plt.xlabel('Valid Date')
plt.ylabel('Score')
# Plot zero-line
plt.axhline(0, 0, data.shape[1], color='k', linestyle='dashed', zorder=0)
# Plot averages of all series
for i, column in enumerate(data):
    plt.axhline(data[column].mean(), 0, xmax=(1 + 15 / len(data)),
                color=colors[i], linestyle='-', linewidth=0.7, clip_on=False)

# Save figure
fig.savefig('rpss_stn.png', dpi=dpi, bbox_inches='tight')
# Display means
print(data.mean())

# ------------------------------------------------------------------------------
# Plot reliability
#
print('\nReliability\n-----------')
# Load CSV
data = pd.read_csv('reliability_stn.csv',
                   parse_dates=['FcstProb'], index_col='FcstProb',
                   skip_blank_lines=True)
# Create empty figure
fig = plt.figure(figsize=(8, 8))
# Plot data
for i, column in enumerate(data):
    ax = data[column].plot(ax=fig.gca(), color=colors[i],
                           linestyle=linestyles[i], linewidth=2)
# Set yticks
plt.yticks(np.arange(0, 1.2, 0.1))
plt.ylim((0, 1.0))
plt.xticks(range(0, data.shape[0]), data.index.values)
plt.xlim((-0.5, 9.5))
# Rotate x-axis labels
plt.setp(ax.get_xticklabels(), rotation=30)
# Plot line of perfect reliability
x = np.arange(0, data.shape[0])
ax.plot(x, x / 10 + 0.05, color='#000000', linewidth=3, clip_on=False,
        label='_nolegend_')
# Set legend properties
legend = ax.legend(borderaxespad=0, loc='upper left')
legend.draw_frame(False)
plt.setp(legend.get_texts(), fontsize='small')
# Draw labels
plt.title('Reliability')
plt.xlabel('Forecast Probability')
plt.ylabel('Observed Frequency')
# Save figure
fig.savefig('reliability_stn.png', dpi=dpi, bbox_inches='tight')
