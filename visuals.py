import plotly
import plotly.graph_objs as go
plotly.offline.init_notebook_mode(connected=True)


def plot_3d_scatter(pca_data, firstComponent, secondComponent, thirdComponent):
    """
        Creates interactive 3D scatter plot for exploring principal components along x, y and z axes.

    Inputs:
        pca_data : DataFrame
            '0' mapped to negative diagnosis.
        firstComponent : String
            e.g. 'PC1'
        secondComponent : String
        thirdComponent : String
    """

    classes = ['Negative diagnosis', 'Positive diagnosis']
    traces = [None] * len(classes)
    scale = ['Reds', 'Blues']

    for i in range(0, len(classes)):
        traces[i] = go.Scatter3d(
            x=pca_data[firstComponent][pca_data.num == i],
            y=pca_data[secondComponent][pca_data.num == i],
            z=pca_data[thirdComponent][pca_data.num == i],
            mode='markers',
            marker=dict(
                color=pca_data[thirdComponent][pca_data.num == i],
                colorscale=scale[i],
                opacity=0.8,
                size=8
            ),
            name=classes[i]
        )

    layout = dict(
        width=800,
        height=700,
        autosize=True,
        title='3D Scatter of {}, {} & {}'.format(firstComponent, secondComponent, thirdComponent),
        scene=dict(
            xaxis=dict(
                title=firstComponent
            ),
            yaxis=dict(
                title=secondComponent
            ),
            zaxis=dict(
                title=thirdComponent
            ),
            aspectratio=dict(x=1, y=1, z=0.7),
            aspectmode='manual',
            camera=dict(
                up=dict(
                    x=0,
                    y=0,
                    z=1
                ),
                eye=dict(
                    x=-1.7428,
                    y=1.0707,
                    z=0.7100,
                ),
            )))

    data = traces
    fig = go.Figure(data=data, layout=layout)

    plotly.offline.iplot(fig, filename='3D PCA Scatter')
