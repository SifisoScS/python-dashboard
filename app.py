from flask import Flask, render_template, jsonify
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
import json
from datetime import datetime, timedelta

app = Flask(__name__)

def generate_sample_data():
    """Generate realistic sample data for the dashboard"""
    
    # Generate dates for the last 30 days
    dates = [datetime.now() - timedelta(days=x) for x in range(30, 0, -1)]
    
    # Sales data with some realistic patterns
    np.random.seed(42)
    base_sales = np.random.normal(10000, 2000, 30)
    trend = np.linspace(0, 3000, 30)
    seasonality = 1000 * np.sin(np.linspace(0, 4*np.pi, 30))
    sales = base_sales + trend + seasonality
    sales = np.maximum(sales, 5000)  # Ensure no negative sales
    
    # Revenue by category
    categories = ['Electronics', 'Clothing', 'Home & Garden', 'Books', 'Sports']
    revenue = [45000, 32000, 28000, 15000, 12000]
    
    # Monthly heatmap data
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    
    # Generate heatmap data with realistic patterns (weekends higher)
    heatmap_data = np.random.randint(50, 200, size=(7, 12))
    heatmap_data[5:7, :] += 100  # Weekend boost
    heatmap_data[4, :] += 50     # Friday boost
    
    return {
        'dates': dates,
        'sales': sales,
        'categories': categories,
        'revenue': revenue,
        'months': months,
        'days': days,
        'heatmap_data': heatmap_data
    }

def create_sales_chart(dates, sales):
    """Create animated sales performance line chart"""
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=dates,
        y=sales,
        mode='lines+markers',
        name='Daily Sales',
        line=dict(color='#6366F1', width=4),
        marker=dict(size=8, color='#818CF8'),
        fill='tozeroy',
        fillcolor='rgba(99, 102, 241, 0.1)'
    ))
    
    fig.update_layout(
        title=dict(
            text='📈 Sales Performance Trend',
            x=0.5,
            font=dict(size=20, color='#1F2937')
        ),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(
            gridcolor='rgba(0,0,0,0.1)',
            title='Date'
        ),
        yaxis=dict(
            gridcolor='rgba(0,0,0,0.1)',
            title='Sales ($)'
        ),
        hovermode='x unified',
        showlegend=False
    )
    
    return json.loads(fig.to_json())

def create_revenue_chart(categories, revenue):
    """Create interactive revenue pie chart"""
    colors = ['#6366F1', '#8B5CF6', '#EC4899', '#10B981', '#F59E0B']
    
    fig = go.Figure(data=[go.Pie(
        labels=categories,
        values=revenue,
        hole=0.4,
        marker=dict(colors=colors),
        textinfo='label+percent',
        hovertemplate='<b>%{label}</b><br>Revenue: $%{value:,.0f}<br>Percentage: %{percent}<extra></extra>'
    )])
    
    fig.update_layout(
        title=dict(
            text='💰 Revenue by Category',
            x=0.5,
            font=dict(size=20, color='#1F2937')
        ),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        showlegend=False,
        annotations=[dict(
            text=f'${sum(revenue):,}',
            x=0.5, y=0.5,
            font_size=20,
            showarrow=False
        )]
    )
    
    return json.loads(fig.to_json())

def create_heatmap_chart(months, days, heatmap_data):
    """Create sales heatmap"""
    fig = go.Figure(data=go.Heatmap(
        z=heatmap_data,
        x=months,
        y=days,
        colorscale='Viridis',
        hoverongaps=False,
        hovertemplate='<b>%{y}</b> in <b>%{x}</b><br>Sales: %{z}<extra></extra>'
    ))
    
    fig.update_layout(
        title=dict(
            text='🔥 Sales Heatmap (Day vs Month)',
            x=0.5,
            font=dict(size=20, color='#1F2937')
        ),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(side='top'),
        height=400
    )
    
    return json.loads(fig.to_json())

@app.route('/')
def index():
    """Main dashboard route"""
    return render_template('index.html')

@app.route('/api/charts')
def get_charts():
    """API endpoint to get all chart data"""
    data = generate_sample_data()
    
    charts = {
        'sales_chart': create_sales_chart(data['dates'], data['sales']),
        'revenue_chart': create_revenue_chart(data['categories'], data['revenue']),
        'heatmap_chart': create_heatmap_chart(data['months'], data['days'], data['heatmap_data'])
    }
    
    return jsonify(charts)

@app.route('/api/stats')
def get_stats():
    """API endpoint to get key statistics"""
    data = generate_sample_data()
    
    stats = {
        'total_revenue': f"${sum(data['revenue']):,}",
        'avg_daily_sales': f"${np.mean(data['sales']):,.0f}",
        'total_categories': len(data['categories']),
        'growth_rate': "+12.5%"
    }
    
    return jsonify(stats)

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'timestamp': datetime.now().isoformat()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)