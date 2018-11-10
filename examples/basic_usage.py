import os

from lendsmart.rest import Client

ACCOUNT_SID = os.environ.get('LENDSMART_ACCOUNT_SID')
AUTH_TOKEN = os.environ.get('LENDSMART_TOKEN')


def example():
    """
    Some example usage of different lendsmart resources.
    """
    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    # Get all documentss
    all_messages = client.documents.list()
    print('There are {} documents in your account.'.format(len(all_messages)))

    # Get all chunks...
    all_chunks = client.prediction_chunks.list()
    print('There are {} chunks in your account.'.format(len(all_chunks)))

    print('Make a document...')
    new_document = client.document.create(to='XXXX', from_='YYYY', body='Lendsmart rocks!')

    print('Making a chunk...')
    new_call = client.prediction_chunks.create(to='XXXX', from_='YYYY', method='GET')


if __name__ == '__main__':
    example()
